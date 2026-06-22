"""E2E tests for CodePipeline — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _localstack_available():
    """Check if localstack is running and serving the codepipeline endpoint."""
    try:
        import urllib.request
        req = urllib.request.Request(f"{ENDPOINT}/_localstack/health")
        req.add_header('Accept', 'application/json')
        urllib.request.urlopen(req, timeout=3)
        # If we got a response, localstack is running
        # Now check if codepipeline endpoint responds
        client = boto3.client('codepipeline', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        client.list_pipelines()
        return True
    except Exception:
        return False


@pytest.mark.skipif(
    not _localstack_available(),
    reason="LocalStack codepipeline endpoint not available (greenfield — ASF provider not written yet)"
)
class TestCodePipelineE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('codepipeline', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Delete test pipelines
        try:
            for p in client.list_pipelines().get('pipelines', []):
                try:
                    client.delete_pipeline(name=p['name'])
                except ClientError:
                    pass
        except ClientError:
            pass

    def test_full_pipeline_crud(self, client):
        """Create → Get → List → Update → Delete pipeline."""
        # 1. Create
        response = client.create_pipeline(pipeline={
            'name': 'test-e2e-pipeline',
            'roleArn': 'arn:aws:iam::000000000000:role/test-role',
            'artifactStore': {'type': 'S3', 'location': 'test-bucket'},
            'stages': [
                {
                    'name': 'Source',
                    'actions': [{
                        'name': 'SourceAction',
                        'actionTypeId': {
                            'category': 'Source',
                            'owner': 'AWS',
                            'provider': 'CodeCommit',
                            'version': '1',
                        },
                        'outputArtifacts': [{'name': 'SourceOutput'}],
                        'configuration': {'BranchName': 'main', 'RepositoryName': 'test'},
                        'runOrder': 1,
                    }],
                },
            ],
        })
        assert response is not None
        assert 'pipeline' in response

        # 2. Get
        response = client.get_pipeline(name='test-e2e-pipeline')
        assert response['pipeline']['name'] == 'test-e2e-pipeline'

        # 3. List
        response = client.list_pipelines()
        names = [p['name'] for p in response['pipelines']]
        assert 'test-e2e-pipeline' in names

        # 4. Update
        client.update_pipeline(pipeline={
            'name': 'test-e2e-pipeline',
            'roleArn': 'arn:aws:iam::000000000000:role/updated-role',
            'artifactStore': {'type': 'S3', 'location': 'test-bucket'},
            'stages': [
                {
                    'name': 'Source',
                    'actions': [{
                        'name': 'SourceAction',
                        'actionTypeId': {
                            'category': 'Source',
                            'owner': 'AWS',
                            'provider': 'CodeCommit',
                            'version': '1',
                        },
                        'outputArtifacts': [{'name': 'SourceOutput'}],
                        'configuration': {'BranchName': 'main', 'RepositoryName': 'test'},
                        'runOrder': 1,
                    }],
                },
            ],
        })
        response = client.get_pipeline(name='test-e2e-pipeline')
        assert response['pipeline']['roleArn'] == 'arn:aws:iam::000000000000:role/updated-role'

        # 5. Start execution
        response = client.start_pipeline_execution(name='test-e2e-pipeline')
        ex_id = response['pipelineExecutionId']
        assert ex_id is not None

        # 6. Get execution
        response = client.get_pipeline_execution(
            pipelineName='test-e2e-pipeline',
            pipelineExecutionId=ex_id,
        )
        assert response['pipelineExecution']['status'] in ('InProgress', 'Succeeded')

        # 7. Delete
        client.delete_pipeline(name='test-e2e-pipeline')

        # 8. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_pipeline(name='test-e2e-pipeline')
        assert exc.value.response['Error']['Code'] == 'PipelineNotFoundException'

    def test_create_duplicate_fails(self, client):
        """Creating duplicate pipeline raises error."""
        client.create_pipeline(pipeline={
            'name': 'test-e2e-dup',
            'roleArn': 'arn:aws:iam::000000000000:role/test-role',
            'artifactStore': {'type': 'S3', 'location': 'test-bucket'},
            'stages': [{
                'name': 'Source',
                'actions': [{
                    'name': 'SourceAction',
                    'actionTypeId': {
                        'category': 'Source', 'owner': 'AWS',
                        'provider': 'CodeCommit', 'version': '1',
                    },
                    'outputArtifacts': [{'name': 'SourceOutput'}],
                    'configuration': {'BranchName': 'main', 'RepositoryName': 'test'},
                    'runOrder': 1,
                }],
            }],
        })
        with pytest.raises(ClientError) as exc:
            client.create_pipeline(pipeline={
                'name': 'test-e2e-dup',
                'roleArn': 'arn:aws:iam::000000000000:role/test-role',
                'artifactStore': {'type': 'S3', 'location': 'test-bucket'},
                'stages': [{
                    'name': 'Source',
                    'actions': [{
                        'name': 'SourceAction',
                        'actionTypeId': {
                            'category': 'Source', 'owner': 'AWS',
                            'provider': 'CodeCommit', 'version': '1',
                        },
                        'outputArtifacts': [{'name': 'SourceOutput'}],
                        'configuration': {'BranchName': 'main', 'RepositoryName': 'test'},
                        'runOrder': 1,
                    }],
                }],
            })
        assert 'PipelineNameInUseException' in exc.value.response['Error']['Code'] or \
               'AlreadyExistsException' in exc.value.response['Error']['Code']

    def test_get_nonexistent_pipeline(self, client):
        """Reading nonexistent pipeline raises error."""
        with pytest.raises(ClientError) as exc:
            client.get_pipeline(name='nonexistent-pipeline')
        assert 'PipelineNotFoundException' in exc.value.response['Error']['Code']

    def test_tags(self, client):
        """Tag → List → Untag."""
        client.create_pipeline(pipeline={
            'name': 'test-e2e-tags',
            'roleArn': 'arn:aws:iam::000000000000:role/test-role',
            'artifactStore': {'type': 'S3', 'location': 'test-bucket'},
            'stages': [{
                'name': 'Source',
                'actions': [{
                    'name': 'SourceAction',
                    'actionTypeId': {
                        'category': 'Source', 'owner': 'AWS',
                        'provider': 'CodeCommit', 'version': '1',
                    },
                    'outputArtifacts': [{'name': 'SourceOutput'}],
                    'configuration': {'BranchName': 'main', 'RepositoryName': 'test'},
                    'runOrder': 1,
                }],
            }],
        })

        # Get pipeline ARN
        pipeline_info = client.get_pipeline(name='test-e2e-tags')
        arn = pipeline_info.get('metadata', {}).get('pipelineArn')
        if arn:
            # Tag
            client.tag_resource(resourceArn=arn, tags=[
                {'Key': 'env', 'Value': 'e2e-test'},
            ])

            # List tags
            response = client.list_tags_for_resource(resourceArn=arn)
            tags = response.get('tags', [])
            assert len(tags) >= 1
            keys = [t['Key'] for t in tags]
            assert 'env' in keys

            # Untag
            client.untag_resource(resourceArn=arn, tagKeys=['env'])

        # Cleanup
        client.delete_pipeline(name='test-e2e-tags')
