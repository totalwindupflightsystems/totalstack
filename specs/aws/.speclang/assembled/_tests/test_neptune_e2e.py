"""E2E test for Neptune — boto3 against running localstack.

NOTE: Neptune is a greenfield TotalStack service. The Neptune provider is not yet
wired into the localstack runtime. E2E tests are skipped until the provider is
registered. The integration tests against the real NeptuneStore validate correctness.
"""
import os

import boto3
import pytest
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test',
              'region_name': 'us-east-1'}


def _neptune_provider_available():
    """Check if localstack has the Neptune provider registered."""
    import urllib.request
    try:
        req = urllib.request.Request(
            f"{ENDPOINT}/_localstack/health",
            headers={'Accept': 'application/json'}
        )
        resp = urllib.request.urlopen(req, timeout=3)
        import json
        data = json.loads(resp.read())
        services = data.get('services', {})
        neptune_state = services.get('neptune', '')
        return neptune_state in ('running', 'available')
    except Exception:
        return False


# Skip all E2E tests until Neptune provider is wired into localstack
pytestmark = pytest.mark.skipif(
    not _neptune_provider_available(),
    reason="Neptune provider not yet wired into localstack — greenfield service"
)


class TestNeptuneE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('neptune', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Clean up test resources
        try:
            client.delete_db_cluster(
                DBClusterIdentifier='e2e-test-cluster',
                SkipFinalSnapshot=True,
            )
        except ClientError:
            pass
        try:
            client.delete_db_cluster_parameter_group(
                DBClusterParameterGroupName='e2e-test-cpg'
            )
        except ClientError:
            pass
        try:
            client.delete_db_subnet_group(
                DBSubnetGroupName='e2e-test-subnet'
            )
        except ClientError:
            pass

    def test_create_describe_delete_cluster(self, client):
        """Create → Describe → Delete workflow for DB cluster."""
        # Create cluster
        response = client.create_db_cluster(
            DBClusterIdentifier='e2e-test-cluster',
            Engine='neptune',
            MasterUsername='admin',
            MasterUserPassword='password123',
        )
        assert response is not None
        assert 'DBCluster' in response
        assert response['DBCluster']['DBClusterIdentifier'] == 'e2e-test-cluster'

        # Describe cluster
        response = client.describe_db_clusters(
            DBClusterIdentifier='e2e-test-cluster'
        )
        clusters = response['DBClusters']
        assert len(clusters) == 1
        assert clusters[0]['Engine'] == 'neptune'

        # Delete cluster
        response = client.delete_db_cluster(
            DBClusterIdentifier='e2e-test-cluster',
            SkipFinalSnapshot=True,
        )
        assert response['DBCluster']['DBClusterIdentifier'] == 'e2e-test-cluster'

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_db_clusters(DBClusterIdentifier='e2e-test-cluster')
        assert exc.value.response['Error']['Code'] == 'DBClusterNotFoundFault'

    def test_create_parameter_group_and_delete(self, client):
        """Create → Describe → Delete workflow for cluster parameter group."""
        # Create
        response = client.create_db_cluster_parameter_group(
            DBClusterParameterGroupName='e2e-test-cpg',
            DBParameterGroupFamily='neptune1.3',
            Description='E2E test parameter group',
        )
        assert 'DBClusterParameterGroup' in response

        # Describe
        response = client.describe_db_cluster_parameter_groups(
            DBClusterParameterGroupName='e2e-test-cpg'
        )
        groups = response['DBClusterParameterGroups']
        assert len(groups) == 1
        assert groups[0]['DBClusterParameterGroupName'] == 'e2e-test-cpg'

        # Delete
        client.delete_db_cluster_parameter_group(
            DBClusterParameterGroupName='e2e-test-cpg'
        )

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_db_cluster_parameter_groups(
                DBClusterParameterGroupName='e2e-test-cpg'
            )
        assert exc.value.response['Error']['Code'] == 'DBClusterParameterGroupNotFoundFault'

    def test_duplicate_cluster_error(self, client):
        """Creating duplicate cluster should fail."""
        client.create_db_cluster(
            DBClusterIdentifier='e2e-test-cluster',
            Engine='neptune',
        )
        try:
            with pytest.raises(ClientError) as exc:
                client.create_db_cluster(
                    DBClusterIdentifier='e2e-test-cluster',
                    Engine='neptune',
                )
            assert exc.value.response['Error']['Code'] in (
                'DBClusterAlreadyExistsFault', 'InvalidParameterValue'
            )
        finally:
            try:
                client.delete_db_cluster(
                    DBClusterIdentifier='e2e-test-cluster',
                    SkipFinalSnapshot=True,
                )
            except ClientError:
                pass
