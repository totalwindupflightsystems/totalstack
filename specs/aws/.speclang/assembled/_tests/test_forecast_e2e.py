"""E2E test for Forecast — boto3 against running localstack (skip if not wired)."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

LS_RUNNING = False
try:
    client = boto3.client('forecast', endpoint_url=ENDPOINT,
                          region_name='us-east-1', **TEST_CREDS)
    client.list_datasets()
    LS_RUNNING = True
except (EndpointConnectionError, ClientError):
    LS_RUNNING = False


class TestForecastE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('forecast', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        if not LS_RUNNING:
            return
        for name in ['e2e-ds', 'e2e-fc', 'e2e-pred']:
            try:
                client.delete_dataset(DatasetArn=f'arn:aws:forecast:us-east-1:123456789012:dataset/{name}')
            except (ClientError, EndpointConnectionError):
                pass
        try:
            client.delete_forecast(ForecastArn='arn:aws:forecast:us-east-1:123456789012:forecast/e2e-fc')
        except (ClientError, EndpointConnectionError):
            pass
        try:
            client.delete_predictor(PredictorArn='arn:aws:forecast:us-east-1:123456789012:predictor/e2e-pred')
        except (ClientError, EndpointConnectionError):
            pass

    def test_dataset_crud(self, client):
        if not LS_RUNNING:
            pytest.skip("Forecast provider not yet wired to LocalStack")
        resp = client.create_dataset(DatasetName='e2e-ds', Domain='CUSTOM',
                                     DatasetType='TARGET_TIME_SERIES', Schema={})
        assert 'DatasetArn' in resp
        client.describe_dataset(DatasetArn=resp['DatasetArn'])
        client.delete_dataset(DatasetArn=resp['DatasetArn'])

    def test_forecast_crud(self, client):
        if not LS_RUNNING:
            pytest.skip("Forecast provider not yet wired to LocalStack")
        resp = client.create_forecast(ForecastName='e2e-fc',
                                      PredictorArn='arn:aws:forecast:us-east-1:123456789012:predictor/fake')
        assert 'ForecastArn' in resp
        client.describe_forecast(ForecastArn=resp['ForecastArn'])
        client.delete_forecast(ForecastArn=resp['ForecastArn'])

    def test_predictor_crud(self, client):
        if not LS_RUNNING:
            pytest.skip("Forecast provider not yet wired to LocalStack")
        resp = client.create_predictor(PredictorName='e2e-pred', ForecastHorizon=10,
                                       InputDataConfig={}, FeaturizationConfig={})
        assert 'PredictorArn' in resp
        client.describe_predictor(PredictorArn=resp['PredictorArn'])
        client.delete_predictor(PredictorArn=resp['PredictorArn'])

    def test_error_nonexistent(self, client):
        if not LS_RUNNING:
            pytest.skip("Forecast provider not yet wired to LocalStack")
        with pytest.raises(ClientError):
            client.describe_dataset(DatasetArn='arn:aws:forecast:us-east-1:123456789012:dataset/fake')
