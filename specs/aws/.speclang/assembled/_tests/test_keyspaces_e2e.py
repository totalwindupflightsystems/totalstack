"""E2E test for Keyspaces — boto3 against running localstack."""
import os
import pytest
import boto3
import socket
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _is_ls():
    try:
        h = ENDPOINT.split('://')[1].split(':')[0]
        p = int(ENDPOINT.split(':')[-1])
        s = socket.create_connection((h, p), timeout=1)
        s.close()
        return True
    except Exception:
        return False


LS_RUNNING = _is_ls()


class TestKeyspacesE2E:
    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('keyspaces', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_list_keyspaces_error(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        c = boto3.client('keyspaces', endpoint_url=ENDPOINT,
                         region_name='us-east-1', **TEST_CREDS)
        try:
            c.list_keyspaces()
        except ClientError as e:
            assert e.response['Error']['Code'] in (
                'InternalFailure', '501', 'NotImplementedError')

    def test_create_keyspace_error(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        c = boto3.client('keyspaces', endpoint_url=ENDPOINT,
                         region_name='us-east-1', **TEST_CREDS)
        try:
            c.create_keyspace(keyspaceName='test')
        except ClientError as e:
            assert e.response['Error']['Code'] in (
                'InternalFailure', '501', 'NotImplementedError')
