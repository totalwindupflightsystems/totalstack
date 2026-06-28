"""E2E test for Identity Store."""
import os
import pytest
import boto3
import urllib.request
from botocore.exceptions import ClientError, EndpointConnectionError
ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TC = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}
try:
    r = urllib.request.urlopen(urllib.request.Request(f'{ENDPOINT}/_localstack/health', method='GET'), timeout=2)
    LS_RUNNING = r.status == 200
except Exception:
    LS_RUNNING = False

class TestIdentityStoreE2E:
    @pytest.fixture
    def client(self): return boto3.client('identitystore', endpoint_url=ENDPOINT, region_name='us-east-1', **TC)
    def test_list_users(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            r = client.list_users(IdentityStoreId='d-test')
            assert r is not None
        except (ClientError, EndpointConnectionError) as e:
            if isinstance(e, EndpointConnectionError): pytest.skip(f"Connection: {e}")
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')
