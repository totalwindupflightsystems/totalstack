"""E2E test for Athena — boto3 against running localstack instance.

To enable: remove the skip marker once the athena provider is wired in localstack.
"""
import os
import pytest
import boto3
import requests
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test',
              'region_name': 'us-east-1'}


def _service_available():
    """Check if athena is available in the running localstack instance."""
    try:
        r = requests.get(f'{ENDPOINT}/_localstack/health', timeout=5)
        return r.json().get('services', {}).get('athena') == 'available'
    except Exception:
        return False


pytestmark = pytest.mark.skipif(
    not _service_available(),
    reason='Athena provider not registered in localstack (greenfield service)'
)


class TestAthenaE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('athena', endpoint_url=ENDPOINT, **TEST_CREDS)

    def test_full_catalog_workflow(self, client):
        """Create → Get → List → Update → Delete a data catalog."""
        # 1. Create
        response = client.create_data_catalog(
            Name='e2e-test-catalog',
            Type='HIVE',
            Description='E2E test catalog'
        )
        assert response is not None

        # 2. Get
        response = client.get_data_catalog(Name='e2e-test-catalog')
        assert response['DataCatalog']['Name'] == 'e2e-test-catalog'
        assert response['DataCatalog']['Type'] == 'HIVE'

        # 3. Update
        response = client.update_data_catalog(
            Name='e2e-test-catalog',
            Type='GLUE',
            Description='Updated E2E catalog'
        )
        assert response['DataCatalog']['Type'] == 'GLUE'

        # 4. Delete
        client.delete_data_catalog(Name='e2e-test-catalog')

        # 5. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_data_catalog(Name='e2e-test-catalog')
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'

    def test_workgroup_crud_workflow(self, client):
        """Create → Get → List → Delete a workgroup."""
        client.create_work_group(Name='e2e-test-wg', Description='E2E workgroup')
        response = client.get_work_group(WorkGroup='e2e-test-wg')
        assert response['WorkGroup']['Name'] == 'e2e-test-wg'
        assert response['WorkGroup']['State'] == 'ENABLED'

        response = client.list_work_groups()
        assert any(wg['Name'] == 'e2e-test-wg' for wg in response['WorkGroups'])

        client.delete_work_group(WorkGroup='e2e-test-wg')
        with pytest.raises(ClientError):
            client.get_work_group(WorkGroup='e2e-test-wg')

    def test_query_execution_workflow(self, client):
        """Start → Get → Stop a query execution."""
        response = client.start_query_execution(QueryString='SELECT 1')
        assert 'QueryExecutionId' in response
        qid = response['QueryExecutionId']

        response = client.get_query_execution(QueryExecutionId=qid)
        assert response['QueryExecution']['Status']['State'] in ('SUCCEEDED', 'RUNNING', 'QUEUED')

        client.stop_query_execution(QueryExecutionId=qid)
        response = client.get_query_execution(QueryExecutionId=qid)
        assert response['QueryExecution']['Status']['State'] == 'CANCELLED'
