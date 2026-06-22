"""E2E tests for AWS Batch — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _localstack_available():
    try:
        import urllib.request
        req = urllib.request.Request(f"{ENDPOINT}/_localstack/health")
        req.add_header('Accept', 'application/json')
        urllib.request.urlopen(req, timeout=3)
        client = boto3.client('batch', endpoint_url=ENDPOINT,
                              region_name='us-east-1', **TEST_CREDS)
        client.describe_compute_environments()
        return True
    except Exception:
        return False


@pytest.mark.skipif(
    not _localstack_available(),
    reason="LocalStack batch endpoint not available (greenfield — ASF provider not written yet)"
)
class TestBatchE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('batch', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        try:
            for ce in client.describe_compute_environments().get('computeEnvironments', []):
                client.update_compute_environment(computeEnvironment=ce['computeEnvironmentName'], state='DISABLED')
                client.delete_compute_environment(computeEnvironment=ce['computeEnvironmentName'])
        except ClientError:
            pass

    def test_compute_environment_crud(self, client):
        resp = client.create_compute_environment(
            computeEnvironmentName='test-e2e-ce',
            type='MANAGED',
            serviceRole='arn:aws:iam::000000000000:role/test',
        )
        assert resp['computeEnvironmentName'] == 'test-e2e-ce'

        resp = client.describe_compute_environments(computeEnvironments=['test-e2e-ce'])
        assert len(resp['computeEnvironments']) == 1

        client.update_compute_environment(computeEnvironment='test-e2e-ce', state='DISABLED')
        resp = client.describe_compute_environments(computeEnvironments=['test-e2e-ce'])
        assert resp['computeEnvironments'][0]['state'] == 'DISABLED'

        client.delete_compute_environment(computeEnvironment='test-e2e-ce')

    def test_job_queue_crud(self, client):
        client.create_compute_environment(
            computeEnvironmentName='test-e2e-jq-ce',
            type='MANAGED',
            serviceRole='arn:aws:iam::000000000000:role/test',
        )
        resp = client.create_job_queue(
            jobQueueName='test-e2e-jq',
            computeEnvironmentOrder=[{'computeEnvironment': 'test-e2e-jq-ce', 'order': 1}],
        )
        assert resp['jobQueueName'] == 'test-e2e-jq'

        resp = client.describe_job_queues(jobQueues=['test-e2e-jq'])
        assert len(resp['jobQueues']) == 1

        client.delete_job_queue(jobQueue='test-e2e-jq')
        client.delete_compute_environment(computeEnvironment='test-e2e-jq-ce')
