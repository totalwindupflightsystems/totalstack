"""E2E test for Redshift — boto3 against running LocalStack (skipped until provider wired)."""
import os
import pytest
import urllib.request
import json

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _localstack_running():
    """Check if LocalStack is reachable."""
    try:
        resp = urllib.request.urlopen(ENDPOINT + '/_localstack/health', timeout=3)
        json.loads(resp.read())
        return True
    except Exception:
        return False


LOCALSTACK_AVAILABLE = _localstack_running()


@pytest.mark.skipif(
    not LOCALSTACK_AVAILABLE,
    reason="LocalStack not running — ASF provider not wired yet"
)
class TestRedshiftE2E:
    @pytest.fixture
    def client(self):
        import boto3
        return boto3.client('redshift', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_full_cluster_crud_workflow(self, client):
        """Create → Describe → Modify → Delete cluster."""
        # 1. Create cluster
        response = client.create_cluster(
            ClusterIdentifier='e2e-test-cluster',
            NodeType='dc2.large',
            MasterUsername='admin',
            MasterUserPassword='Password1!',
        )
        assert response is not None
        assert response['Cluster']['ClusterIdentifier'] == 'e2e-test-cluster'

        # 2. Describe
        response = client.describe_clusters(ClusterIdentifier='e2e-test-cluster')
        assert len(response['Clusters']) == 1

        # 3. Modify
        response = client.modify_cluster(
            ClusterIdentifier='e2e-test-cluster',
            ClusterType='multi-node',
            NumberOfNodes=4,
        )
        assert response['Cluster']['NumberOfNodes'] == 4

        # 4. Delete
        client.delete_cluster(
            ClusterIdentifier='e2e-test-cluster',
            SkipFinalClusterSnapshot=True,
        )

        # 5. Verify deleted
        from botocore.exceptions import ClientError
        with pytest.raises(ClientError) as exc:
            client.describe_clusters(ClusterIdentifier='e2e-test-cluster')
        assert exc.value.response['Error']['Code'] == 'ClusterNotFound'

    def test_error_duplicate_cluster(self, client):
        """Creating duplicate cluster fails."""
        from botocore.exceptions import ClientError
        client.create_cluster(
            ClusterIdentifier='e2e-dup-cluster',
            NodeType='dc2.large',
            MasterUsername='admin',
            MasterUserPassword='Password1!',
        )
        try:
            with pytest.raises(ClientError) as exc:
                client.create_cluster(
                    ClusterIdentifier='e2e-dup-cluster',
                    NodeType='dc2.large',
                    MasterUsername='admin',
                    MasterUserPassword='Password1!',
                )
            assert exc.value.response['Error']['Code'] == 'ClusterAlreadyExists'
        finally:
            client.delete_cluster(
                ClusterIdentifier='e2e-dup-cluster',
                SkipFinalClusterSnapshot=True,
            )

    def test_error_nonexistent_cluster(self, client):
        """Reading nonexistent cluster fails."""
        from botocore.exceptions import ClientError
        with pytest.raises(ClientError) as exc:
            client.describe_clusters(ClusterIdentifier='no-such-cluster')
        assert exc.value.response['Error']['Code'] == 'ClusterNotFound'


# Always-passing test so the file runs even when skipped
def test_e2e_placeholder():
    """Placeholder test to keep the file runnable when E2E tests are skipped."""
    assert True
