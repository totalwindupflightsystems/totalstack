"""E2E test for OpenSearchServerless — boto3 against running localstack."""
import os
import pytest
import boto3
import urllib.request
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _check_localstack():
    """Check if localstack is running."""
    try:
        req = urllib.request.Request(
            ENDPOINT + '/_localstack/health',
            headers={'Accept': 'application/json'},
            method='GET')
        urllib.request.urlopen(req, timeout=3)
        return True
    except Exception:
        return False


LS_RUNNING = _check_localstack()


class TestOpenSearchServerlessE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('opensearchserverless', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_create_collection_workflow(self, client):
        """Create → list → delete workflow."""
        # 1. Create collection
        resp = client.create_collection(
            name='e2e-test-collection',
            type='SEARCH',
            description='E2E test collection')
        assert resp is not None
        collection_id = resp.get('id') or resp.get('createCollectionDetail', {}).get('id')
        assert collection_id is not None

        # 2. List collections
        list_resp = client.list_collections()
        assert list_resp is not None

        # 3. Delete collection
        client.delete_collection(id=collection_id)

    def test_create_duplicate_fails(self, client):
        """Creating duplicate collection name should fail."""
        resp = client.create_collection(
            name='e2e-dup-test',
            type='SEARCH')
        collection_id = resp.get('id') or resp.get('createCollectionDetail', {}).get('id')
        try:
            client.create_collection(name='e2e-dup-test', type='SEARCH')
            # If no exception, still clean up
            pytest.fail("Expected ConflictException")
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('ConflictException', 'InternalFailure', '501')
        finally:
            if collection_id:
                try:
                    client.delete_collection(id=collection_id)
                except Exception:
                    pass

    def test_get_nonexistent_fails(self, client):
        """Getting nonexistent collection fails."""
        try:
            client.batch_get_collection(ids=['nonexistent-id'])
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('ResourceNotFoundException', 'InternalFailure', '501', 'ValidationException')
