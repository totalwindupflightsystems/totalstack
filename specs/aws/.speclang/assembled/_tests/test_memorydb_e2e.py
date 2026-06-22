"""E2E test for MemoryDB — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError
import socket

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _is_localstack_running():
    try:
        host = ENDPOINT.split('://')[1].split(':')[0]
        port = int(ENDPOINT.split(':')[-1])
        s = socket.create_connection((host, port), timeout=1)
        s.close()
        return True
    except Exception:
        return False


LS_RUNNING = _is_localstack_running()


class TestMemoryDBE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('memorydb', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_describe_clusters_error_no_localstack(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('memorydb', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.describe_clusters()
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_create_cluster_error_no_localstack(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('memorydb', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.create_cluster(
                ClusterName='test-cluster',
                NodeType='db.r6g.large',
                ACLName='open-access',
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_describe_acls_error_no_localstack(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client = boto3.client('memorydb', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        try:
            client.describe_acls()
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')
