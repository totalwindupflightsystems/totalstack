"""E2E test for Personalize — skip if not wired."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError
E = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TC = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}
LS = False
try:
    c = boto3.client('personalize', endpoint_url=E, region_name='us-east-1', **TC)
    c.list_datasets()
    LS = True
except (EndpointConnectionError, ClientError): pass

class TestPersonalizeE2E:
    @pytest.fixture
    def client(self): return boto3.client('personalize', endpoint_url=E, region_name='us-east-1', **TC)

    def test_dataset_crud(self, client):
        if not LS: pytest.skip("Personalize provider not wired")
        client.create_dataset(name='e2e-ds', schemaArn='arn:s', datasetGroupArn='arn:g', datasetType='Interactions')
        client.describe_dataset(datasetArn='arn:aws:personalize:us-east-1:123456789012:dataset/e2e-ds')
        client.delete_dataset(datasetArn='arn:aws:personalize:us-east-1:123456789012:dataset/e2e-ds')

    def test_error_nonexistent(self, client):
        if not LS: pytest.skip("Personalize provider not wired")
        with pytest.raises(ClientError):
            client.describe_dataset(datasetArn='arn:aws:personalize:us-east-1:123456789012:dataset/fake')
