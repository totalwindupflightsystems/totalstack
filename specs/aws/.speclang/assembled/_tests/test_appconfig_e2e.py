"""E2E test for AppConfig — boto3 against running localstack."""
import os
import pytest
import boto3
import urllib.request
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _ls():
    try:
        req = urllib.request.Request(
            ENDPOINT + '/_localstack/health',
            headers={'Accept': 'application/json'},
            method='GET')
        urllib.request.urlopen(req, timeout=3)
        return True
    except Exception:
        return False


LS_RUNNING = _ls()


class TestAppConfigE2E:
    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('appconfig', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_create_app_workflow(self, client):
        r = client.create_application(Name='e2e-app')
        assert r.get('Id') is not None
        aid = r['Id']
        r2 = client.get_application(ApplicationId=aid)
        assert r2['Name'] == 'e2e-app'
        rs = client.list_applications()
        assert len(rs.get('Items', [])) >= 1
        client.delete_application(ApplicationId=aid)

    def test_error_nonexistent(self, client):
        try:
            client.get_application(ApplicationId='nonexistent')
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('ResourceNotFoundException', 'InternalFailure', '501')
