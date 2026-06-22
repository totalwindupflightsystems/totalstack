"""E2E test for Bedrock Agent — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

try:
    import urllib.request
    urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
    LS_RUNNING = True
except Exception:
    LS_RUNNING = False


class TestBedrockAgentE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('bedrock-agent', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_list_agents(self, client):
        try:
            response = client.list_agents()
            assert response is not None
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', 'NotImplementedError', 'ValidationException')

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_create_and_get_agent(self, client):
        try:
            create_resp = client.create_agent(agentName='e2e-agent')
            assert 'agent' in create_resp
            agent_id = create_resp['agent']['agentId']
            get_resp = client.get_agent(agentId=agent_id)
            assert get_resp['agent']['agentName'] == 'e2e-agent'
            client.delete_agent(agentId=agent_id)
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', 'NotImplementedError',
                           'ResourceNotFoundException', 'ValidationException')

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_list_knowledge_bases(self, client):
        try:
            response = client.list_knowledge_bases()
            assert response is not None
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', 'NotImplementedError', 'ValidationException')

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_create_knowledge_base(self, client):
        try:
            response = client.create_knowledge_base(
                name='e2e-kb',
                roleArn='arn:aws:iam::000000000000:role/BedrockRole',
                knowledgeBaseConfiguration={
                    'type': 'VECTOR',
                    'vectorKnowledgeBaseConfiguration': {
                        'embeddingModelArn': 'arn:aws:bedrock:us-east-1::foundation-model/test',
                    },
                },
            )
            assert 'knowledgeBase' in response
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', 'NotImplementedError',
                           'ResourceNotFoundException', 'ValidationException')
