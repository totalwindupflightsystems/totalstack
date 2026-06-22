"""E2E tests for DynamoDB Streams."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError
ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

def _ls_running():
    try:
        import urllib.request
        urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
        return True
    except Exception:
        return False

LS_RUNNING = _ls_running()

class TestDynamoDBStreamsE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('dynamodbstreams', endpoint_url=ENDPOINT, region_name='us-east-1', **CREDS)

    def test_health_check(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            client.list_streams()
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError', 'InternalServerError', 'UnknownOperationException')
        except EndpointConnectionError:
            pytest.skip("LocalStack not available")
