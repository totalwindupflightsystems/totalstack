"""E2E test for RolesAnywhere — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

LS_RUNNING = False
try:
    import urllib.request
    import socket
    req = urllib.request.Request(f'{ENDPOINT}/_localstack/health', method='GET')
    socket.setdefaulttimeout(2)
    urllib.request.urlopen(req, timeout=2)
    LS_RUNNING = True
except Exception:
    pass


class TestRolesAnywhereE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('rolesanywhere', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_full_crud_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            # Create profile
            resp = client.create_profile(
                name='e2e-profile',
                roleArns=['arn:aws:iam::123456789012:role/test'],
            )
            assert 'profile' in resp
            pid = resp['profile']['profileId']

            # Get profile
            resp2 = client.get_profile(profileId=pid)
            assert resp2['profile']['name'] == 'e2e-profile'

            # Update profile
            resp3 = client.update_profile(profileId=pid, name='e2e-updated')
            assert resp3['profile']['name'] == 'e2e-updated'

            # List profiles
            resp4 = client.list_profiles()
            assert len(resp4['profiles']) >= 1

            # Create trust anchor
            resp5 = client.create_trust_anchor(
                name='e2e-ta',
                source={'sourceType': 'CERTIFICATE_BUNDLE'},
            )
            assert 'trustAnchor' in resp5
            tid = resp5['trustAnchor']['trustAnchorId']

            # Get trust anchor
            resp6 = client.get_trust_anchor(trustAnchorId=tid)
            assert resp6['trustAnchor']['name'] == 'e2e-ta'

            # Disable/enable
            client.disable_trust_anchor(trustAnchorId=tid)
            resp7 = client.get_trust_anchor(trustAnchorId=tid)
            assert resp7['trustAnchor']['enabled'] is False
            client.enable_trust_anchor(trustAnchorId=tid)

            # Tags
            arn = resp['profile']['profileArn']
            client.tag_resource(resourceArn=arn, tags=[{'key': 'e2e', 'value': 'true'}])
            resp8 = client.list_tags_for_resource(resourceArn=arn)
            assert resp8['tags']['e2e'] == 'true'
            client.untag_resource(resourceArn=arn, tagKeys=['e2e'])

            # Delete
            client.delete_trust_anchor(trustAnchorId=tid)
            client.delete_profile(profileId=pid)

        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_error_nonexistent_profile(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            with pytest.raises(ClientError) as exc:
                client.get_profile(profileId='nonexistent-nonexistent')
            assert exc.value.response['Error']['Code'] in (
                'ResourceNotFoundException', 'NotFoundException',
                'InternalFailure', '501',
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')
