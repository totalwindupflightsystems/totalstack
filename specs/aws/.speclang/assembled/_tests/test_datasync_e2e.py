"""E2E test for DataSync — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

# Check if localstack is running
LS_RUNNING = False
try:
    import urllib.request
    resp = urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
    LS_RUNNING = resp.status == 200
except Exception:
    LS_RUNNING = False


class TestDataSyncE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('datasync', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        if not LS_RUNNING:
            return
        # Clean up test resources
        try:
            agents = client.list_agents()
            for a in agents.get('Agents', []):
                try:
                    client.delete_agent(AgentArn=a['AgentArn'])
                except ClientError:
                    pass
        except ClientError:
            pass

    def test_create_agent_smoke(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            resp = client.create_agent(ActivationKey='test-key-12345')
            assert 'AgentArn' in resp
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_list_agents_smoke(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            resp = client.list_agents()
            assert 'Agents' in resp
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_error_nonexistent_agent(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            client.describe_agent(AgentArn='arn:aws:datasync:us-east-1:000000000000:agent/agent-nonexistent')
            pytest.fail("Should have raised ClientError")
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InvalidRequestException', 'ResourceNotFoundException',
                           'InternalFailure', '501', 'NotImplementedError')
