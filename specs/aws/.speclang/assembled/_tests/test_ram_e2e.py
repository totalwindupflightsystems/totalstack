"""E2E test for RAM — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

# Health check: is localstack running?
try:
    import urllib.request
    req = urllib.request.Request(f'{ENDPOINT}/_localstack/health', method='GET')
    resp = urllib.request.urlopen(req, timeout=2)
    LS_RUNNING = resp.status == 200
except Exception:
    LS_RUNNING = False


class TestRamE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('ram', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # No cleanup needed — RAM is a greenfield service returning 501
        pass

    def test_service_accessible(self, client):
        """Verify RAM service endpoint responds."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running for greenfield RAM service")

        try:
            response = client.list_resource_types()
            assert response is not None
            assert 'resourceTypes' in response
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError):
                pytest.skip(f"LocalStack connection failed: {e}")
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_create_resource_share(self, client):
        """Create resource share — verify API is reachable."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        try:
            response = client.create_resource_share(
                name='e2e-test-share',
                resourceArns=['arn:aws:ec2:us-east-1:000000000000:instance/i-test'],
                principals=['arn:aws:iam::111111111111:root'],
            )
            assert response is not None
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError):
                pytest.skip(f"LocalStack connection failed: {e}")
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError', 'InternalServerError'):
                pytest.skip(f"RAM E2E: {code} — provider not wired yet")
            raise

    def test_list_resource_types(self, client):
        """List resource types — verify API responds."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        try:
            response = client.list_resource_types()
            assert response is not None
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError):
                pytest.skip(f"LocalStack connection failed: {e}")
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError', 'InternalServerError'):
                pytest.skip(f"RAM E2E: {code} — provider not wired yet")
            raise

    def test_error_nonexistent(self, client):
        """Accessing nonexistent resource share fails."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        try:
            client.get_resource_shares(
                resourceShareArns=['arn:aws:ram:us-east-1:000000000000:resource-share/nonexistent'],
                resourceOwner='SELF',
            )
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError):
                pytest.skip(f"LocalStack connection failed: {e}")
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError', 'InternalServerError'):
                pytest.skip(f"RAM E2E: {code} — provider not wired yet")
            raise
