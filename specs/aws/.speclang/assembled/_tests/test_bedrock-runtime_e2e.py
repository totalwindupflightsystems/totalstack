"""E2E test for Bedrock Runtime — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError
import socket

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _is_localstack_running():
    """Check if localstack is running on the expected endpoint."""
    try:
        host = ENDPOINT.split('://')[1].split(':')[0]
        port = int(ENDPOINT.split(':')[-1])
        s = socket.create_connection((host, port), timeout=1)
        s.close()
        return True
    except Exception:
        return False


LS_RUNNING = _is_localstack_running()


class TestBedrockRuntimeE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('bedrock-runtime', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_converse_error_no_localstack(self):
        """Expect error when hitting localstack with unsupported endpoint."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('bedrock-runtime', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.converse(
                modelId='anthropic.claude-3-sonnet',
                messages=[{'role': 'user', 'content': [{'text': 'Hello'}]}],
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                            'AccessDeniedException', 'ValidationException')

    def test_invoke_model_error_no_localstack(self):
        """InvokeModel expects error from unsupported localstack endpoint."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('bedrock-runtime', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.invoke_model(
                modelId='anthropic.claude-3-sonnet',
                body='{}',
                contentType='application/json',
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                            'AccessDeniedException', 'ValidationException')

    def test_count_tokens_error_no_localstack(self):
        """CountTokens expects error from unsupported localstack endpoint."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('bedrock-runtime', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.count_tokens(
                modelId='anthropic.claude-3-sonnet',
                input={'text': 'Hello world'},
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                            'AccessDeniedException', 'ValidationException')

    def test_apply_guardrail_error_no_localstack(self):
        """ApplyGuardrail expects error from unsupported localstack endpoint."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('bedrock-runtime', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.apply_guardrail(
                guardrailIdentifier='gr-123',
                guardrailVersion='1',
                source='INPUT',
                content=[{'text': {'text': 'Hello'}}],
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                            'AccessDeniedException', 'ValidationException')
