"""E2E tests for ElastiCache — boto3 against running localstack.

CURRENT STATUS: Greenfield service with no LocalStack provider.
E2E tests auto-skip until the provider is wired.
"""
import os
import pytest
import boto3
from botocore.exceptions import ClientError
import urllib.request

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {
    'aws_access_key_id': 'test',
    'aws_secret_access_key': 'test',
    'region_name': 'us-east-1',
}


def _localstack_available():
    """Check if localstack is running and has the elasticache service."""
    try:
        resp = urllib.request.urlopen(
            urllib.request.Request(
                f'{ENDPOINT}/_localstack/health',
                headers={'Accept': 'application/json'},
            ),
            timeout=3,
        )
        import json
        health = json.loads(resp.read())
        services = health.get('services', {})
        elasticache_status = services.get('elasticache', 'unavailable')
        running = elasticache_status in ('running', 'available')
        return running
    except Exception:
        return False


@pytest.mark.skipif(
    not _localstack_available(),
    reason='ElastiCache provider not yet wired to localstack'
)
class TestElastiCacheE2E:
    """Full E2E workflow tests — only run when provider is wired."""

    @pytest.fixture
    def client(self):
        return boto3.client('elasticache', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Clean up test resources
        for cluster_id in ['e2e-test-cluster', 'e2e-test-cluster-2']:
            try:
                client.delete_cache_cluster(CacheClusterId=cluster_id)
            except ClientError:
                pass
        for rg_id in ['e2e-test-rg']:
            try:
                client.delete_replication_group(ReplicationGroupId=rg_id)
            except ClientError:
                pass

    def test_full_crud_workflow(self, client):
        """Create → describe → modify → delete a cache cluster."""
        # 1. Create cache cluster
        response = client.create_cache_cluster(
            CacheClusterId='e2e-test-cluster',
            Engine='redis',
            CacheNodeType='cache.t2.micro',
            NumCacheNodes=1,
        )
        assert response['CacheCluster']['CacheClusterId'] == 'e2e-test-cluster'
        assert response['CacheCluster']['CacheClusterStatus'] == 'available'

        # 2. Describe
        response = client.describe_cache_clusters(
            CacheClusterId='e2e-test-cluster',
        )
        assert len(response['CacheClusters']) == 1

        # 3. Modify
        response = client.modify_cache_cluster(
            CacheClusterId='e2e-test-cluster',
            CacheNodeType='cache.t3.micro',
        )
        assert response['CacheCluster']['CacheNodeType'] == 'cache.t3.micro'

        # 4. Delete
        client.delete_cache_cluster(CacheClusterId='e2e-test-cluster')

        # 5. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_cache_clusters(CacheClusterId='e2e-test-cluster')
        assert exc.value.response['Error']['Code'] == 'CacheClusterNotFound'

    def test_error_duplicate_create(self, client):
        """Creating duplicate cache cluster fails."""
        client.create_cache_cluster(
            CacheClusterId='e2e-test-cluster-2',
            Engine='redis',
            CacheNodeType='cache.t2.micro',
            NumCacheNodes=1,
        )
        with pytest.raises(ClientError) as exc:
            client.create_cache_cluster(
                CacheClusterId='e2e-test-cluster-2',
                Engine='redis',
                CacheNodeType='cache.t2.micro',
                NumCacheNodes=1,
            )
        assert exc.value.response['Error']['Code'] == 'CacheClusterAlreadyExists'

    def test_error_nonexistent_read(self, client):
        """Reading nonexistent cache cluster fails."""
        with pytest.raises(ClientError):
            client.describe_cache_clusters(
                CacheClusterId='nonexistent-cluster',
            )

    def test_replication_group_workflow(self, client):
        """Create → describe → delete a replication group."""
        # Create
        response = client.create_replication_group(
            ReplicationGroupId='e2e-test-rg',
            ReplicationGroupDescription='E2E test replication group',
            Engine='redis',
        )
        assert response['ReplicationGroup']['ReplicationGroupId'] == 'e2e-test-rg'

        # Describe
        response = client.describe_replication_groups(
            ReplicationGroupId='e2e-test-rg',
        )
        assert len(response['ReplicationGroups']) == 1

        # Delete
        client.delete_replication_group(ReplicationGroupId='e2e-test-rg')

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_replication_groups(ReplicationGroupId='e2e-test-rg')
        assert exc.value.response['Error']['Code'] == 'ReplicationGroupNotFound'
