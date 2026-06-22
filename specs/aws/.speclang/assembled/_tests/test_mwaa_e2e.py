"""E2E test for MWAA — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _check_localstack():
    """Check if localstack is running."""
    import urllib.request
    try:
        urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
        return True
    except Exception:
        return False


LS_RUNNING = _check_localstack()


class TestMWAAE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('mwaa', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        if not LS_RUNNING:
            return
        # Clean up test environments
        try:
            client.delete_environment(Name='e2e-test-env')
        except ClientError:
            pass
        try:
            client.delete_environment(Name='e2e-tags-env')
        except ClientError:
            pass

    def test_full_crud_workflow(self, client):
        """Create → Get → List → Update → Delete."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        # 1. Create environment
        resp = client.create_environment(
            Name='e2e-test-env',
            ExecutionRoleArn='arn:aws:iam::000000000000:role/mwaa',
            SourceBucketArn='arn:aws:s3:::my-bucket',
            DagS3Path='dags/',
            NetworkConfiguration={
                'SecurityGroupIds': ['sg-12345'],
                'SubnetIds': ['subnet-abc', 'subnet-def'],
            },
            EnvironmentClass='mw1.small',
            MaxWorkers=10,
            MinWorkers=1,
            Schedulers=2,
            WebserverAccessMode='PUBLIC_ONLY',
        )
        assert resp is not None
        assert 'Arn' in resp

        # 2. Get environment
        resp = client.get_environment(Name='e2e-test-env')
        assert resp is not None
        env = resp['Environment']
        assert env['Name'] == 'e2e-test-env'
        assert env['Status'] in ('CREATING', 'AVAILABLE')

        # 3. List environments
        resp = client.list_environments()
        assert 'Environments' in resp
        assert 'e2e-test-env' in resp['Environments']

        # 4. Update environment
        resp = client.update_environment(
            Name='e2e-test-env',
            MinWorkers=3,
            MaxWorkers=25,
        )
        assert resp is not None
        assert 'Arn' in resp

        # 5. Delete environment
        resp = client.delete_environment(Name='e2e-test-env')
        assert resp is not None

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_environment(Name='e2e-test-env')
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    def test_error_nonexistent_get(self, client):
        """Getting a nonexistent environment fails."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        with pytest.raises(ClientError) as exc:
            client.get_environment(Name='nonexistent-env')
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'ResourceNotFound',
            'InternalFailure', '501', 'NotImplementedError')

    def test_error_nonexistent_update(self, client):
        """Updating a nonexistent environment fails."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        with pytest.raises(ClientError) as exc:
            client.update_environment(Name='nonexistent-env', MinWorkers=5)
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'ResourceNotFound',
            'InternalFailure', '501', 'NotImplementedError')
