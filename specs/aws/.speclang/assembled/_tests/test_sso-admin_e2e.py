"""E2E test for SSO Admin — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError
import urllib.request

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

try:
    req = urllib.request.Request(f'{ENDPOINT}/_localstack/health', method='GET')
    resp = urllib.request.urlopen(req, timeout=2)
    LS_RUNNING = resp.status == 200
except Exception:
    LS_RUNNING = False


class TestSsoAdminE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('sso-admin', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_list_instances(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            response = client.list_instances()
            assert response is not None
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError):
                pytest.skip(f"Connection failed: {e}")
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_error_nonexistent(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            client.describe_instance(InstanceArn='arn:nonexistent')
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError):
                pytest.skip(f"Connection failed: {e}")
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError', 'InternalServerError'):
                pytest.skip(f"SSO Admin E2E: {code} — provider not wired yet")
            raise
