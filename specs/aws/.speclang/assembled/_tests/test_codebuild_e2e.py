"""E2E tests for CodeBuild — boto3 against running localstack.
Uses skipif pattern for greenfield services until provider is wired.
"""
import os
import json
import pytest
import boto3
import urllib.request
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {
    'aws_access_key_id': 'test',
    'aws_secret_access_key': 'test',
    'region_name': 'us-east-1',
}


def _localstack_healthy():
    """Check if localstack is running and has codebuild provider."""
    try:
        url = f"{ENDPOINT}/_localstack/health"
        with urllib.request.urlopen(url, timeout=3) as resp:
            health = json.loads(resp.read().decode())
            services = health.get('services', {})
            cb = services.get('codebuild', '')
            return cb in ('running', 'available')
    except Exception:
        return False


CODEBUILD_AVAILABLE = _localstack_healthy()


@pytest.mark.skipif(
    not CODEBUILD_AVAILABLE,
    reason="CodeBuild provider not yet wired in LocalStack"
)
class TestCodeBuildE2E:
    """End-to-end tests for CodeBuild via boto3."""

    @pytest.fixture
    def client(self):
        return boto3.client('codebuild', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Clean up test projects
        try:
            client.delete_project(name='e2e-test-project')
        except ClientError:
            pass
        try:
            client.delete_project(name='e2e-dup-project')
        except ClientError:
            pass

    def test_full_crud_workflow(self, client):
        """Create → describe → verify → delete a project."""
        # 1. Create project
        response = client.create_project(
            name='e2e-test-project',
            source={'type': 'S3', 'location': 'bucket/source.zip'},
            environment={
                'type': 'LINUX_CONTAINER',
                'image': 'aws/codebuild/standard:5.0',
                'computeType': 'BUILD_GENERAL1_SMALL',
            },
            artifacts={'type': 'NO_ARTIFACTS'},
            serviceRole='arn:aws:iam::123456789012:role/CodeBuildRole',
            description='E2E test project',
        )
        assert response is not None
        assert 'project' in response
        assert response['project']['name'] == 'e2e-test-project'
        assert response['project']['arn'].startswith('arn:aws:codebuild:')

        # 2. Read project
        response = client.batch_get_projects(names=['e2e-test-project'])
        assert len(response['projects']) == 1
        assert response['projects'][0]['name'] == 'e2e-test-project'

        # 3. List projects
        response = client.list_projects()
        assert 'projects' in response
        assert 'e2e-test-project' in response['projects']

        # 4. Start a build
        build_resp = client.start_build(projectName='e2e-test-project')
        assert 'build' in build_resp
        build_id = build_resp['build']['id']
        assert build_resp['build']['buildStatus'] == 'IN_PROGRESS'

        # 5. Stop the build
        stop_resp = client.stop_build(id=build_id)
        assert stop_resp['build']['buildStatus'] == 'STOPPED'

        # 6. Delete project
        client.delete_project(name='e2e-test-project')

        # 7. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.batch_get_projects(names=['e2e-test-project'])
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    def test_error_duplicate_create(self, client):
        """Creating duplicate project fails."""
        args = {
            'name': 'e2e-dup-project',
            'source': {'type': 'S3', 'location': 'x/y.zip'},
            'environment': {
                'type': 'LINUX_CONTAINER',
                'image': 'aws/codebuild/standard:5.0',
                'computeType': 'BUILD_GENERAL1_SMALL',
            },
            'artifacts': {'type': 'NO_ARTIFACTS'},
            'serviceRole': 'arn:aws:iam::123456789012:role/CodeBuildRole',
        }
        client.create_project(**args)

        with pytest.raises(ClientError) as exc:
            client.create_project(**args)
        assert exc.value.response['Error']['Code'] == 'ResourceAlreadyExistsException'

    def test_error_nonexistent_read(self, client):
        """Reading nonexistent project fails."""
        with pytest.raises(ClientError) as exc:
            client.batch_get_projects(names=['nonexistent-project'])
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    def test_error_nonexistent_start_build(self, client):
        """Starting build on nonexistent project fails."""
        with pytest.raises(ClientError) as exc:
            client.start_build(projectName='nonexistent-project')
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'
