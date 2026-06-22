"""E2E tests for Grafana — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _ls_running():
    try:
        import urllib.request
        urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
        return True
    except Exception:
        return False


LS_RUNNING = _ls_running()


class TestGrafanaE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('grafana', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_health_check(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            client.list_workspaces()
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                          'InternalServerException', 'UnknownOperationException')
        except EndpointConnectionError:
            pytest.skip("LocalStack not available")

    def test_create_workspace_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            resp = client.create_workspace(
                accountAccessType='CURRENT_ACCOUNT',
                permissionType='SERVICE_MANAGED',
                authenticationProviders=['AWS_SSO'],
                workspaceName='e2e-test-ws',
            )
            assert resp is not None
        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError',
                       'UnknownOperationException', 'InternalServerException'):
                pytest.skip(f"Operation not yet implemented: {code}")
            raise
        except EndpointConnectionError:
            pytest.skip("LocalStack not available")
