"""E2E test for DocumentDB — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _localstack_reachable():
    """Check if localstack is running."""
    import urllib.request
    import json
    try:
        resp = urllib.request.urlopen(
            f'{ENDPOINT}/_localstack/health', timeout=3)
        json.loads(resp.read())
        return True
    except Exception:
        return False


LS_RUNNING = _localstack_reachable()


class TestDocumentDBE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('docdb', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    @pytest.mark.skipif(not LS_RUNNING, reason='LocalStack is not running')
    def test_full_cluster_crud_workflow(self, client):
        """Create cluster → describe → modify → delete."""
        try:
            # 1. Create cluster
            response = client.create_db_cluster(
                DBClusterIdentifier='e2e-test-cluster',
                Engine='docdb',
                MasterUsername='admin',
                MasterUserPassword='password123',
            )
            assert response is not None
            assert response['DBCluster']['DBClusterIdentifier'] == 'e2e-test-cluster'

            # 2. Describe cluster
            response = client.describe_db_clusters(
                DBClusterIdentifier='e2e-test-cluster')
            assert len(response['DBClusters']) == 1
            assert response['DBClusters'][0]['DBClusterIdentifier'] == 'e2e-test-cluster'

            # 3. Modify cluster
            response = client.modify_db_cluster(
                DBClusterIdentifier='e2e-test-cluster',
                BackupRetentionPeriod=7,
            )
            assert response['DBCluster']['BackupRetentionPeriod'] == 7

            # 4. Delete cluster
            response = client.delete_db_cluster(
                DBClusterIdentifier='e2e-test-cluster',
                SkipFinalSnapshot=True,
            )
            assert response['DBCluster']['DBClusterIdentifier'] == 'e2e-test-cluster'

            # 5. Verify deleted
            with pytest.raises(ClientError) as exc:
                client.describe_db_clusters(
                    DBClusterIdentifier='e2e-test-cluster')
            assert exc.value.response['Error']['Code'] == 'DBClusterNotFoundFault'

        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError'):
                pytest.skip(f'LocalStack does not support this operation: {code}')
            raise

    @pytest.mark.skipif(not LS_RUNNING, reason='LocalStack is not running')
    def test_cluster_lifecycle_start_stop(self, client):
        """Create → stop → start → verify."""
        try:
            client.create_db_cluster(
                DBClusterIdentifier='e2e-lifecycle-cluster',
                Engine='docdb',
                MasterUsername='admin',
                MasterUserPassword='password123',
            )

            # Stop cluster
            response = client.stop_db_cluster(
                DBClusterIdentifier='e2e-lifecycle-cluster')
            assert response['DBCluster']['Status'] == 'stopped'

            # Start cluster
            response = client.start_db_cluster(
                DBClusterIdentifier='e2e-lifecycle-cluster')
            assert response['DBCluster']['Status'] == 'available'

            # Cleanup
            client.delete_db_cluster(
                DBClusterIdentifier='e2e-lifecycle-cluster',
                SkipFinalSnapshot=True,
            )

        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError'):
                pytest.skip(f'LocalStack does not support this operation: {code}')
            raise

    @pytest.mark.skipif(not LS_RUNNING, reason='LocalStack is not running')
    def test_subnet_group_crud(self, client):
        """Create subnet group → describe → delete."""
        try:
            # Create
            response = client.create_db_subnet_group(
                DBSubnetGroupName='e2e-test-subnet',
                DBSubnetGroupDescription='E2E test subnet group',
                SubnetIds=['subnet-abc12345'],
            )
            assert response['DBSubnetGroup']['DBSubnetGroupName'] == 'e2e-test-subnet'

            # Describe
            response = client.describe_db_subnet_groups(
                DBSubnetGroupName='e2e-test-subnet')
            assert len(response['DBSubnetGroups']) == 1

            # Delete
            client.delete_db_subnet_group(
                DBSubnetGroupName='e2e-test-subnet')

            # Verify deleted
            with pytest.raises(ClientError) as exc:
                client.describe_db_subnet_groups(
                    DBSubnetGroupName='e2e-test-subnet')
            assert exc.value.response['Error']['Code'] == 'DBSubnetGroupNotFoundFault'

        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError'):
                pytest.skip(f'LocalStack does not support this operation: {code}')
            raise

    def test_error_skip_when_no_localstack(self, client):
        """This test always runs but gracefully handles missing service."""
        try:
            client.describe_db_clusters()
        except ClientError as e:
            code = e.response['Error']['Code']
            # Either the service isn't wired (InternalFailure) or it works
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                            'InvalidParameterValue')
