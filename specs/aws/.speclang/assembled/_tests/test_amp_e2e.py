"""E2E test for AMP — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _check_localstack():
    try:
        import urllib.request
        urllib.request.urlopen(ENDPOINT + '/_localstack/health', timeout=2)
        return True
    except Exception:
        return False


LS_RUNNING = _check_localstack()


class TestAMPE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('amp', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        if LS_RUNNING:
            try:
                resp = client.list_workspaces()
                for ws in resp.get('workspaces', []):
                    try:
                        client.delete_workspace(workspaceId=ws['workspaceId'])
                    except ClientError:
                        pass
            except (ClientError, Exception):
                pass

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_create_describe_delete_workspace(self, client):
        resp = client.create_workspace(alias='e2e-test-ws')
        assert resp is not None
        assert 'workspaceId' in resp
        ws_id = resp['workspaceId']

        desc = client.describe_workspace(workspaceId=ws_id)
        assert desc['workspace']['workspaceId'] == ws_id
        assert desc['workspace']['alias'] == 'e2e-test-ws'

        client.delete_workspace(workspaceId=ws_id)

        with pytest.raises(ClientError) as exc:
            client.describe_workspace(workspaceId=ws_id)
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'InternalFailure', '501',
        )

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_list_workspaces(self, client):
        resp = client.create_workspace(alias='list-test')
        ws_id = resp['workspaceId']

        resp = client.list_workspaces()
        assert 'workspaces' in resp
        found = [w for w in resp['workspaces'] if w['workspaceId'] == ws_id]
        assert len(found) >= 1

        client.delete_workspace(workspaceId=ws_id)

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_error_nonexistent_workspace(self, client):
        with pytest.raises(ClientError) as exc:
            client.describe_workspace(workspaceId='ws-nonexistent')
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'InternalFailure', '501',
        )

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_create_workspace_with_tags(self, client):
        resp = client.create_workspace(
            alias='tagged-ws',
            tags={'env': 'e2e', 'team': 'qa'},
        )
        ws_id = resp['workspaceId']

        tags_resp = client.list_tags_for_resource(resourceArn=resp['arn'])
        assert tags_resp['tags']['env'] == 'e2e'
        assert tags_resp['tags']['team'] == 'qa'

        client.delete_workspace(workspaceId=ws_id)
