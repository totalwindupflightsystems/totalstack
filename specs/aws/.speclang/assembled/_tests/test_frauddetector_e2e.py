"""E2E test for FraudDetector — skip if not wired."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError
E = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TC = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}
LS = False
try:
    c = boto3.client('frauddetector', endpoint_url=E, region_name='us-east-1', **TC)
    c.get_detectors()
    LS = True
except (EndpointConnectionError, ClientError): pass

class TestFraudDetectorE2E:
    @pytest.fixture
    def client(self): return boto3.client('frauddetector', endpoint_url=E, region_name='us-east-1', **TC)

    def test_detector_crud(self, client):
        if not LS: pytest.skip("FraudDetector provider not wired")
        client.put_detector(detectorId='e2e-d', eventTypeName='t')
        client.describe_detector(detectorId='e2e-d')
        client.delete_detector(detectorId='e2e-d')

    def test_variable_crud(self, client):
        if not LS: pytest.skip("FraudDetector provider not wired")
        client.create_variable(name='e2e-v', dataType='STRING', dataSource='EVENT', defaultValue='x')
        client.get_variables(name='e2e-v')
        client.delete_variable(name='e2e-v')

    def test_error_nonexistent(self, client):
        if not LS: pytest.skip("FraudDetector provider not wired")
        with pytest.raises(ClientError):
            client.describe_detector(detectorId='nonexistent')
