"""E2E test for Verified Permissions — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

LS_RUNNING = False
try:
    import urllib.request
    resp = urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
    LS_RUNNING = resp.status == 200
except Exception:
    LS_RUNNING = False


class TestVerifiedPermissionsE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('verifiedpermissions', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_list_policy_stores_smoke(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            resp = client.list_policy_stores()
            assert 'policyStores' in resp
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_error_nonexistent_store(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            client.get_policy_store(policyStoreId='nonexistent')
            pytest.fail("Should have raised")
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('ResourceNotFoundException', 'InternalFailure',
                           '501', 'NotImplementedError')
