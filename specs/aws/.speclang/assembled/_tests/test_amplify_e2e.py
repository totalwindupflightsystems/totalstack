"""E2E tests for Amplify — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

def _ls_running():
    try:
        import urllib.request
        urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
        return True
    except Exception:
        return False

LS_RUNNING = _ls_running()


class TestAmplifyE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('amplify', endpoint_url=ENDPOINT, region_name='us-east-1', **CREDS)

    def test_full_app_crud(self, client):
        resp = client.create_app(name='e2e-app')
        assert resp['app']['name'] == 'e2e-app'
        app_id = resp['app']['appId']

        resp = client.get_app(appId=app_id)
        assert resp['app']['appId'] == app_id

        resp = client.update_app(appId=app_id, description='updated')
        assert resp['app']['description'] == 'updated'

        client.delete_app(appId=app_id)
        with pytest.raises(ClientError) as exc:
            client.get_app(appId=app_id)
        assert 'NotFound' in exc.value.response['Error']['Code']

    def test_full_branch_crud(self, client):
        resp = client.create_app(name='br-e2e-app')
        app_id = resp['app']['appId']
        try:
            resp = client.create_branch(appId=app_id, branchName='main')
            assert resp['branch']['branchName'] == 'main'

            resp = client.get_branch(appId=app_id, branchName='main')
            assert resp['branch']['branchName'] == 'main'

            client.delete_branch(appId=app_id, branchName='main')
            with pytest.raises(ClientError):
                client.get_branch(appId=app_id, branchName='main')
        finally:
            client.delete_app(appId=app_id)
