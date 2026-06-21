"""E2E test for RDS — boto3 against running localstack."""
import os
import pytest
import urllib.request

try:
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    boto3 = None
    ClientError = None

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {
    'aws_access_key_id': 'test',
    'aws_secret_access_key': 'test',
    'region_name': 'us-east-1',
}


def _localstack_running():
    """Check if localstack health endpoint is reachable."""
    try:
        urllib.request.urlopen(
            f"{ENDPOINT}/_localstack/health", timeout=2)
        return True
    except Exception:
        return False


def _rds_available():
    """Check if RDS service is available in running localstack."""
    if not _localstack_running():
        return False
    try:
        client = boto3.client('rds', endpoint_url=ENDPOINT, **TEST_CREDS)
        client.describe_db_instances()
        return True
    except Exception:
        return False


# Skip E2E tests until RDS provider is wired into LocalStack
pytestmark = pytest.mark.skipif(
    not _rds_available(),
    reason='RDS provider not yet wired into LocalStack')


@pytest.mark.skipif(boto3 is None, reason='boto3 not installed')
class TestRDSE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('rds', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Clean up test resources
        for identifier in ['test-e2e-db', 'test-e2e-cluster']:
            try:
                client.delete_db_instance(
                    DBInstanceIdentifier=identifier,
                    SkipFinalSnapshot=True)
            except ClientError:
                pass
            try:
                client.delete_db_cluster(
                    DBClusterIdentifier=identifier,
                    SkipFinalSnapshot=True)
            except ClientError:
                pass
        for name in ['test-e2e-pg', 'test-e2e-sg', 'test-e2e-cpg']:
            try:
                client.delete_db_parameter_group(DBParameterGroupName=name)
            except ClientError:
                pass
            try:
                client.delete_db_subnet_group(DBSubnetGroupName=name)
            except ClientError:
                pass
            try:
                client.delete_db_cluster_parameter_group(
                    DBClusterParameterGroupName=name)
            except ClientError:
                pass

    def test_full_db_instance_crud_workflow(self, client):
        """Create → describe → modify → delete a DB instance."""
        # 1. Create DB parameter group (prerequisite)
        client.create_db_parameter_group(
            DBParameterGroupName='test-e2e-pg',
            DBParameterGroupFamily='mysql8.0',
            Description='E2E test parameter group',
        )

        # 2. Create DB instance
        response = client.create_db_instance(
            DBInstanceIdentifier='test-e2e-db',
            DBInstanceClass='db.t3.micro',
            Engine='mysql',
            MasterUsername='admin',
            MasterUserPassword='password123',
            AllocatedStorage=20,
            DBParameterGroupName='test-e2e-pg',
        )
        assert response['DBInstance']['DBInstanceIdentifier'] == 'test-e2e-db'
        assert response['DBInstance']['Engine'] == 'mysql'
        assert response['DBInstance']['DBInstanceStatus'] == 'available'

        # 3. Describe DB instance
        response = client.describe_db_instances(
            DBInstanceIdentifier='test-e2e-db')
        instances = response['DBInstances']
        assert len(instances) == 1
        assert instances[0]['DBInstanceIdentifier'] == 'test-e2e-db'

        # 4. Modify DB instance
        response = client.modify_db_instance(
            DBInstanceIdentifier='test-e2e-db',
            DBInstanceClass='db.t3.small',
        )
        assert response['DBInstance']['DBInstanceIdentifier'] == 'test-e2e-db'

        # 5. Delete DB instance
        response = client.delete_db_instance(
            DBInstanceIdentifier='test-e2e-db',
            SkipFinalSnapshot=True,
        )
        assert response['DBInstance']['DBInstanceIdentifier'] == 'test-e2e-db'

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_db_instances(DBInstanceIdentifier='test-e2e-db')
        assert exc.value.response['Error']['Code'] == 'DBInstanceNotFound'

        # Cleanup parameter group
        client.delete_db_parameter_group(DBParameterGroupName='test-e2e-pg')

    def test_db_cluster_workflow(self, client):
        """Create → describe → delete a DB cluster."""
        # Create cluster parameter group (prerequisite)
        client.create_db_cluster_parameter_group(
            DBClusterParameterGroupName='test-e2e-cpg',
            DBParameterGroupFamily='aurora-mysql8.0',
            Description='E2E test cluster parameter group',
        )

        # Create DB subnet group (prerequisite)
        client.create_db_subnet_group(
            DBSubnetGroupName='test-e2e-sg',
            DBSubnetGroupDescription='E2E test subnet group',
            SubnetIds=['subnet-abc123', 'subnet-def456'],
        )

        # Create DB cluster
        response = client.create_db_cluster(
            DBClusterIdentifier='test-e2e-cluster',
            Engine='aurora-mysql',
            MasterUsername='admin',
            MasterUserPassword='password123',
            DBClusterParameterGroupName='test-e2e-cpg',
            DBSubnetGroupName='test-e2e-sg',
        )
        assert response['DBCluster']['DBClusterIdentifier'] == 'test-e2e-cluster'
        assert response['DBCluster']['Status'] == 'available'

        # Describe cluster
        response = client.describe_db_clusters(
            DBClusterIdentifier='test-e2e-cluster')
        assert len(response['DBClusters']) == 1

        # Delete cluster
        response = client.delete_db_cluster(
            DBClusterIdentifier='test-e2e-cluster',
            SkipFinalSnapshot=True,
        )
        assert response['DBCluster']['DBClusterIdentifier'] == 'test-e2e-cluster'

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_db_clusters(DBClusterIdentifier='test-e2e-cluster')
        assert exc.value.response['Error']['Code'] == 'DBClusterNotFound'

        # Cleanup
        client.delete_db_cluster_parameter_group(
            DBClusterParameterGroupName='test-e2e-cpg')
        client.delete_db_subnet_group(DBSubnetGroupName='test-e2e-sg')

    def test_error_handling(self, client):
        """Error paths for invalid operations."""
        # Describe nonexistent instance
        with pytest.raises(ClientError) as exc:
            client.describe_db_instances(
                DBInstanceIdentifier='nonexistent-db')
        assert exc.value.response['Error']['Code'] == 'DBInstanceNotFound'

        # Delete nonexistent instance
        with pytest.raises(ClientError) as exc:
            client.delete_db_instance(DBInstanceIdentifier='nonexistent-db')
        assert exc.value.response['Error']['Code'] == 'DBInstanceNotFound'

        # Create with invalid parameter
        with pytest.raises(ClientError) as exc:
            client.create_db_instance(
                DBInstanceIdentifier='invalid-db',
                DBInstanceClass='invalid-class',
                Engine='mysql',
            )
        assert exc.value.response['Error']['Code'] in (
            'InvalidParameterValue', 'InvalidParameterCombination')
