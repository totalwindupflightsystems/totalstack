"""E2E tests for Comprehend — boto3 against running localstack."""
import os
import pytest
import boto3

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

def _ls_running():
    try:
        import urllib.request
        urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
        return True
    except Exception:
        return False

LS_RUNNING = _ls_running()

class TestComprehendE2E:
    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('comprehend', endpoint_url=ENDPOINT, region_name='us-east-1', **CREDS)

    def test_detect_sentiment(self, client):
        resp = client.detect_sentiment(Text='I love AWS', LanguageCode='en')
        assert resp['Sentiment'] in ('POSITIVE', 'NEGATIVE', 'NEUTRAL', 'MIXED')

    def test_detect_entities(self, client):
        resp = client.detect_entities(Text='AWS is great', LanguageCode='en')
        assert 'Entities' in resp
