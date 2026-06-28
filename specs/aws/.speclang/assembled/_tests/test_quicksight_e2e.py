"""E2E test for QuickSight — boto3 against running localstack.

QuickSight has no LocalStack ASF provider yet — tests gracefully skip if
LocalStack is not running or returns 501.
"""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

LS_RUNNING = False
try:
    client = boto3.client('quicksight', endpoint_url=ENDPOINT,
                          region_name='us-east-1', **TEST_CREDS)
    client.list_data_sets(AwsAccountId='123456789012')
    LS_RUNNING = True
except (EndpointConnectionError, ClientError):
    LS_RUNNING = False


class TestQuickSightE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('quicksight', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        if not LS_RUNNING:
            return
        try:
            client.delete_data_set(AwsAccountId='123456789012', DataSetId='qs-e2e-dataset')
        except (ClientError, EndpointConnectionError):
            pass
        try:
            client.delete_dashboard(AwsAccountId='123456789012', DashboardId='qs-e2e-dashboard')
        except (ClientError, EndpointConnectionError):
            pass

    def test_dataset_crud_workflow(self, client):
        """Create → describe → update → delete a DataSet."""
        if not LS_RUNNING:
            pytest.skip("QuickSight provider not yet wired to LocalStack")

        # Create
        resp = client.create_data_set(
            AwsAccountId='123456789012',
            DataSetId='qs-e2e-dataset',
            Name='E2E Test Dataset',
            PhysicalTableMap={},
            ImportMode='SPICE',
        )
        assert resp['Status'] == 200
        assert resp['DataSetId'] == 'qs-e2e-dataset'

        # Describe
        resp = client.describe_data_set(
            AwsAccountId='123456789012',
            DataSetId='qs-e2e-dataset',
        )
        assert resp['DataSetId'] == 'qs-e2e-dataset'

        # List
        resp = client.list_data_sets(AwsAccountId='123456789012')
        assert resp['Status'] == 200

        # Update
        resp = client.update_data_set(
            AwsAccountId='123456789012',
            DataSetId='qs-e2e-dataset',
            Name='Updated DS',
            PhysicalTableMap={},
            ImportMode='SPICE',
        )
        assert resp['Status'] == 200

        # Delete
        resp = client.delete_data_set(
            AwsAccountId='123456789012',
            DataSetId='qs-e2e-dataset',
        )
        assert resp['Status'] == 200

    def test_dashboard_crud_workflow(self, client):
        """Create → describe → delete a Dashboard."""
        if not LS_RUNNING:
            pytest.skip("QuickSight provider not yet wired to LocalStack")

        resp = client.create_dashboard(
            AwsAccountId='123456789012',
            DashboardId='qs-e2e-dashboard',
            Name='E2E Test Dashboard',
        )
        assert resp['Status'] == 200

        resp = client.describe_dashboard(
            AwsAccountId='123456789012',
            DashboardId='qs-e2e-dashboard',
        )
        assert resp['DashboardId'] == 'qs-e2e-dashboard'

        resp = client.delete_dashboard(
            AwsAccountId='123456789012',
            DashboardId='qs-e2e-dashboard',
        )
        assert resp['Status'] == 200

    def test_error_nonexistent_resource(self, client):
        """Read nonexistent DataSet returns ResourceNotFound."""
        if not LS_RUNNING:
            pytest.skip("QuickSight provider not yet wired to LocalStack")

        with pytest.raises(ClientError) as exc:
            client.describe_data_set(
                AwsAccountId='123456789012',
                DataSetId='nonexistent-qs',
            )
        assert exc.value.response['Error']['Code'] in (
            'ResourceNotFoundException', 'NotFound', 'ResourceNotFound',
            'InvalidParameterValueException',
        )

    def test_error_duplicate_create(self, client):
        """Creating duplicate DataSet fails."""
        if not LS_RUNNING:
            pytest.skip("QuickSight provider not yet wired to LocalStack")

        kwargs = {
            'AwsAccountId': '123456789012',
            'DataSetId': 'qs-e2e-dup',
            'Name': 'Duplicate Test',
            'PhysicalTableMap': {},
            'ImportMode': 'SPICE',
        }
        client.create_data_set(**kwargs)
        try:
            with pytest.raises(ClientError) as exc:
                client.create_data_set(**kwargs)
            assert exc.value.response['Error']['Code'] in (
                'ResourceExistsException', 'ConflictException',
                'ResourceAlreadyExistsException',
            )
        finally:
            client.delete_data_set(AwsAccountId='123456789012', DataSetId='qs-e2e-dup')
