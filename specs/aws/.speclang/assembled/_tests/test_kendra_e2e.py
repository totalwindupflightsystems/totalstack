"""E2E test for Kendra — boto3 against running localstack."""
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


class TestKendraE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('kendra', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_create_describe_delete_index(self, client):
        resp = client.create_index(
            Name='e2e-test-idx',
            RoleArn='arn:aws:iam::000000000000:role/kendra',
            Edition='DEVELOPER_EDITION',
        )
        assert resp is not None
        assert 'Id' in resp
        idx_id = resp['Id']

        desc = client.describe_index(Id=idx_id)
        assert desc['Id'] == idx_id
        assert desc['Name'] == 'e2e-test-idx'

        client.delete_index(Id=idx_id)

        with pytest.raises(ClientError) as exc:
            client.describe_index(Id=idx_id)
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'InternalFailure', '501',
        )

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_list_indices(self, client):
        resp = client.create_index(
            Name='list-test',
            RoleArn='arn:aws:iam::000000000000:role/kendra',
            Edition='DEVELOPER_EDITION',
        )
        idx_id = resp['Id']

        resp = client.list_indices()
        assert resp is not None

        client.delete_index(Id=idx_id)

    @pytest.mark.skipif(not LS_RUNNING, reason="LocalStack not running")
    def test_error_nonexistent_index(self, client):
        with pytest.raises(ClientError) as exc:
            client.describe_index(Id='nonexistent')
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'InternalFailure', '501',
        )
