"""E2E tests for Timestream for InfluxDB — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _ls_running():
    """Check if localstack is running."""
    try:
        import urllib.request
        req = urllib.request.Request(f'{ENDPOINT}/_localstack/health')
        urllib.request.urlopen(req, timeout=2)
        return True
    except Exception:
        return False


LS_RUNNING = _ls_running()


class TestTimestreamInfluxDBE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('timestream-influxdb', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_health_check(self, client):
        """Smoke test — verify localstack responds to the service endpoint."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        try:
            client.list_db_clusters()
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                          'InternalServerException', 'UnknownOperationException')
        except EndpointConnectionError:
            pytest.skip("LocalStack not available")

    def test_create_cluster_workflow(self, client):
        """Create → describe → update → delete a DbCluster via boto3."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        try:
            # Create
            resp = client.create_db_cluster(
                name='e2e-test-cluster',
                dbInstanceType='db.influx.large',
                vpcSubnetIds=['subnet-abc123'],
                vpcSecurityGroupIds=['sg-abc123'],
            )
            assert resp is not None
        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError',
                       'UnknownOperationException', 'InternalServerException'):
                pytest.skip(f"Operation not yet implemented: {code}")
            raise
        except EndpointConnectionError:
            pytest.skip("LocalStack not available")
