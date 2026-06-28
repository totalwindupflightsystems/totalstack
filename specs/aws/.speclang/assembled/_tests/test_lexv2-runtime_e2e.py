"""E2E test for Lex V2 Runtime — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

LS_RUNNING = False
try:
    import urllib.request
    urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
    LS_RUNNING = True
except Exception:
    pass

BOT = "BOT123"
ALIAS = "ALIAS456"
LOCALE = "en_US"
SESSION = "e2e-session"


class TestLexV2RuntimeE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('lexv2-runtime', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_session_crud_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client.put_session(
            botId=BOT, botAliasId=ALIAS, localeId=LOCALE,
            sessionId=SESSION, sessionState={"state": "started"})
        resp = client.get_session(
            botId=BOT, botAliasId=ALIAS, localeId=LOCALE,
            sessionId=SESSION)
        assert resp["sessionId"] == SESSION
        client.delete_session(
            botId=BOT, botAliasId=ALIAS, localeId=LOCALE,
            sessionId=SESSION)

    def test_recognize_text(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client.put_session(
            botId=BOT, botAliasId=ALIAS, localeId=LOCALE,
            sessionId=SESSION)
        resp = client.recognize_text(
            botId=BOT, botAliasId=ALIAS, localeId=LOCALE,
            sessionId=SESSION, text="Hello!")
        assert "messages" in resp

    def test_error_nonexistent(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        with pytest.raises(ClientError) as exc:
            client.get_session(
                botId=BOT, botAliasId=ALIAS, localeId=LOCALE,
                sessionId="nonexistent-session")
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'
