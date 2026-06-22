"""E2E test for Kafka (MSK) — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _check_localstack():
    import urllib.request
    try:
        urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
        return True
    except Exception:
        return False


LS_RUNNING = _check_localstack()


class TestKafkaE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('kafka', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_full_cluster_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        resp = client.create_cluster(
            ClusterName='e2e-test',
            BrokerNodeGroupInfo={
                'ClientSubnets': ['subnet-abc'],
                'InstanceType': 'kafka.m5.large',
                'SecurityGroups': ['sg-123'],
            },
            KafkaVersion='3.6.0',
            NumberOfBrokerNodes=3,
        )
        assert 'ClusterArn' in resp

        resp = client.describe_cluster(ClusterArn=resp['ClusterArn'])
        assert resp['ClusterInfo']['ClusterName'] == 'e2e-test'

        client.delete_cluster(ClusterArn=resp['ClusterInfo']['ClusterArn'])

    def test_error_nonexistent(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")

        with pytest.raises(ClientError) as exc:
            client.describe_cluster(ClusterArn='arn:nonexistent')
        assert exc.value.response['Error']['Code'] in (
            'NotFoundException', 'ResourceNotFound', 'InternalFailure', '501')
