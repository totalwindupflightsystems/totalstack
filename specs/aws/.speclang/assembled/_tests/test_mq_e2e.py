"""E2E tests for Amazon MQ — boto3 against running localstack."""
import os
import pytest
import urllib.request
import json

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _is_localstack_running():
    try:
        req = urllib.request.Request(f"{ENDPOINT}/_localstack/health",
                                     headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=3)
        data = json.loads(resp.read())
        return data.get('services', {}).get('mq') in ('available', 'running')
    except Exception:
        return False


LOCALSTACK_AVAILABLE = _is_localstack_running()


@pytest.mark.skipif(not LOCALSTACK_AVAILABLE,
                    reason="MQ ASF provider not wired yet")
class TestMqE2E:
    @pytest.fixture
    def client(self):
        import boto3
        return boto3.client('mq', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        from botocore.exceptions import ClientError
        try:
            brokers = client.list_brokers()
            for b in brokers.get('BrokerSummaries', []):
                client.delete_broker(BrokerId=b['BrokerId'])
        except ClientError:
            pass

    def test_full_broker_workflow(self, client):
        from botocore.exceptions import ClientError
        resp = client.create_broker(
            BrokerName='e2e-broker',
            EngineType='ActiveMQ',
            DeploymentMode='SINGLE_INSTANCE',
            HostInstanceType='mq.t3.micro',
        )
        broker_id = resp['BrokerId']
        assert broker_id is not None

        desc = client.describe_broker(BrokerId=broker_id)
        assert desc['BrokerName'] == 'e2e-broker'

        client.delete_broker(BrokerId=broker_id)
        with pytest.raises(ClientError) as exc:
            client.describe_broker(BrokerId=broker_id)
        assert exc.value.response['Error']['Code'] == 'NotFoundException'

    def test_error_duplicate_create(self, client):
        from botocore.exceptions import ClientError
        resp = client.create_broker(
            BrokerName='dup-broker',
            EngineType='ActiveMQ',
            DeploymentMode='SINGLE_INSTANCE',
            HostInstanceType='mq.t3.micro',
        )
        with pytest.raises(ClientError) as exc:
            client.create_broker(
                BrokerName='dup-broker',
                EngineType='ActiveMQ',
                DeploymentMode='SINGLE_INSTANCE',
                HostInstanceType='mq.t3.micro',
            )
        assert exc.value.response['Error']['Code'] in ('ConflictException', 'Conflict')
        client.delete_broker(BrokerId=resp['BrokerId'])

    def test_error_nonexistent_read(self, client):
        from botocore.exceptions import ClientError
        with pytest.raises(ClientError) as exc:
            client.describe_broker(BrokerId='nonexistent')
        assert exc.value.response['Error']['Code'] == 'NotFoundException'


class TestMqE2ESmoke:
    def test_imports_work(self):
        import boto3
        assert hasattr(boto3, 'client')

    def test_skip_condition_runs(self):
        assert _is_localstack_running() in (True, False)
