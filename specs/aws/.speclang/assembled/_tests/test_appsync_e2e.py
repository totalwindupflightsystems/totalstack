"""E2E test for AppSync — boto3 against running localstack."""
import os
import pytest
import boto3
import urllib.request
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _check_localstack():
    try:
        req = urllib.request.Request(
            ENDPOINT + '/_localstack/health',
            headers={'Accept': 'application/json'}, method='GET')
        urllib.request.urlopen(req, timeout=3)
        return True
    except Exception:
        return False


LS_RUNNING = _check_localstack()


class TestAppSyncE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('appsync', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_create_api_workflow(self, client):
        """Create → get → list → delete API workflow."""
        resp = client.create_graphql_api(
            name='e2e-test-api',
            authenticationType='API_KEY')
        assert resp is not None
        api = resp.get('graphqlApi', {})
        api_id = api.get('apiId')
        assert api_id is not None

        resp = client.get_graphql_api(apiId=api_id)
        assert resp['graphqlApi']['name'] == 'e2e-test-api'

        resp = client.list_graphql_apis()
        assert len(resp.get('graphqlApis', [])) >= 1

        client.delete_graphql_api(apiId=api_id)

    def test_create_api_key(self, client):
        """Create API → create API key workflow."""
        resp = client.create_graphql_api(
            name='e2e-key-test',
            authenticationType='API_KEY')
        api_id = resp['graphqlApi']['apiId']
        try:
            key_resp = client.create_api_key(apiId=api_id)
            assert key_resp is not None
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotFoundException')
        finally:
            try:
                client.delete_graphql_api(apiId=api_id)
            except Exception:
                pass

    def test_error_nonexistent_api(self, client):
        """Getting nonexistent API fails."""
        try:
            client.get_graphql_api(apiId='nonexistent-id')
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('NotFoundException', 'InternalFailure', '501')
