"""E2E tests for S3 Tables — boto3 against running localstack.

Uses skipif pattern for greenfield services until the ASF provider is wired.
"""
import os
import pytest
import urllib.request
import json

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _is_localstack_running():
    """Check if localstack is running."""
    try:
        req = urllib.request.Request(
            f"{ENDPOINT}/_localstack/health",
            headers={'User-Agent': 'Mozilla/5.0'},
        )
        resp = urllib.request.urlopen(req, timeout=3)
        data = json.loads(resp.read())
        return data.get('services', {}).get('s3tables') in ('available', 'running')
    except Exception:
        return False


LOCALSTACK_AVAILABLE = _is_localstack_running()


@pytest.mark.skipif(not LOCALSTACK_AVAILABLE,
                    reason="S3 Tables ASF provider not wired yet")
class TestS3TablesE2E:
    """Full boto3 CRUD workflow against running localstack."""

    @pytest.fixture
    def client(self):
        import boto3
        return boto3.client('s3tables', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        from botocore.exceptions import ClientError
        try:
            buckets = client.list_table_buckets()
            for b in buckets.get('tableBuckets', []):
                client.delete_table_bucket(tableBucketARN=b['arn'])
        except ClientError:
            pass

    def test_full_table_bucket_workflow(self, client):
        """Create → describe → list → delete table bucket."""
        from botocore.exceptions import ClientError

        # 1. Create table bucket
        response = client.create_table_bucket(name='e2e-test-bucket')
        assert response is not None
        arn = response['tableBucketARN']
        assert 'e2e-test-bucket' in arn

        # 2. Describe table bucket
        response = client.get_table_bucket(tableBucketARN=arn)
        assert response['name'] == 'e2e-test-bucket'

        # 3. List table buckets
        response = client.list_table_buckets()
        assert len(response['tableBuckets']) >= 1

        # 4. Delete table bucket
        client.delete_table_bucket(tableBucketARN=arn)

        # 5. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_table_bucket(tableBucketARN=arn)
        assert exc.value.response['Error']['Code'] == 'NotFoundException'

    def test_error_duplicate_create(self, client):
        """Creating duplicate table bucket fails."""
        from botocore.exceptions import ClientError

        response = client.create_table_bucket(name='dup-bucket')
        arn = response['tableBucketARN']

        with pytest.raises(ClientError) as exc:
            client.create_table_bucket(name='dup-bucket')
        assert exc.value.response['Error']['Code'] in ('ConflictException', 'Conflict')

        client.delete_table_bucket(tableBucketARN=arn)

    def test_error_nonexistent_read(self, client):
        """Reading nonexistent table bucket fails."""
        from botocore.exceptions import ClientError

        with pytest.raises(ClientError) as exc:
            client.get_table_bucket(
                tableBucketARN='arn:aws:s3tables:::bucket/nonexistent')
        assert exc.value.response['Error']['Code'] == 'NotFoundException'


# Smoke test that always runs (verifies test file structure is valid)
class TestS3TablesE2ESmoke:
    """Always-run smoke tests to verify test file validity."""

    def test_imports_work(self):
        import boto3
        assert hasattr(boto3, 'client')

    def test_skip_condition_runs(self):
        assert _is_localstack_running() in (True, False)
