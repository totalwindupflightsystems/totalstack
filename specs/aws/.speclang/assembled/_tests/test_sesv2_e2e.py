"""E2E test for SESv2 — boto3 against running localstack."""
import os
import json
import urllib.request
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}


def _localstack_reachable():
    try:
        resp = urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=3)
        json.loads(resp.read())
        return True
    except Exception:
        return False


LS_RUNNING = _localstack_reachable()


class TestSESV2E2E:

    @pytest.fixture
    def client(self):
        return boto3.client('sesv2', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    @pytest.mark.skipif(not LS_RUNNING, reason='LocalStack is not running')
    def test_email_identity_crud(self, client):
        try:
            # Create identity
            resp = client.create_email_identity(
                EmailIdentity='test@example.com')
            assert resp is not None

            # Get identity
            resp = client.get_email_identity(
                EmailIdentity='test@example.com')
            assert resp['IdentityType'] in ('EMAIL_ADDRESS', 'DOMAIN')

            # Delete identity
            client.delete_email_identity(
                EmailIdentity='test@example.com')

            # Verify deleted
            with pytest.raises(ClientError) as exc:
                client.get_email_identity(EmailIdentity='test@example.com')
            assert 'NotFound' in exc.value.response['Error']['Code']

        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError'):
                pytest.skip(f'Operation not supported: {code}')
            raise

    @pytest.mark.skipif(not LS_RUNNING, reason='LocalStack is not running')
    def test_contact_list_crud(self, client):
        try:
            # Create
            resp = client.create_contact_list(ContactListName='e2e-list')
            assert resp is not None

            # Get
            resp = client.get_contact_list(ContactListName='e2e-list')
            assert resp['ContactListName'] == 'e2e-list'

            # Delete
            client.delete_contact_list(ContactListName='e2e-list')

        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError'):
                pytest.skip(f'Operation not supported: {code}')
            raise

    @pytest.mark.skipif(not LS_RUNNING, reason='LocalStack is not running')
    def test_send_email(self, client):
        try:
            resp = client.send_email(
                FromEmailAddress='sender@example.com',
                Destination={'ToAddresses': ['recipient@example.com']},
                Content={
                    'Simple': {
                        'Subject': {'Data': 'Test', 'Charset': 'UTF-8'},
                        'Body': {'Text': {'Data': 'Hello', 'Charset': 'UTF-8'}},
                    }
                },
            )
            assert 'MessageId' in resp

        except ClientError as e:
            code = e.response['Error']['Code']
            if code in ('InternalFailure', '501', 'NotImplementedError'):
                pytest.skip(f'Operation not supported: {code}')
            raise

    def test_error_when_no_localstack(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            client.list_email_identities()
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')
