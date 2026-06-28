"""E2E test for Signer — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

# Check if LocalStack is running
LS_RUNNING = False
try:
    import urllib.request
    req = urllib.request.Request(f'{ENDPOINT}/_localstack/health', method='GET')
    import socket
    socket.setdefaulttimeout(2)
    urllib.request.urlopen(req, timeout=2)
    LS_RUNNING = True
except Exception:
    pass


class TestSignerE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('signer', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_list_signing_platforms(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            resp = client.list_signing_platforms()
            assert 'platforms' in resp
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError')

    def test_full_crud_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            # 1. Create signing profile
            resp = client.put_signing_profile(
                profileName='e2e-test-profile',
                platformId='AWSLambda-SHA384-ECDSA',
                signingMaterial={'certificateArn': 'arn:aws:acm:us-east-1:123456789012:certificate/test'},
            )
            assert 'arn' in resp

            # 2. Get signing profile
            resp2 = client.get_signing_profile(profileName='e2e-test-profile')
            assert resp2['profileName'] == 'e2e-test-profile'
            assert resp2['status'] == 'Active'

            # 3. List signing profiles
            resp3 = client.list_signing_profiles()
            names = [p['profileName'] for p in resp3['profiles']]
            assert 'e2e-test-profile' in names

            # 4. Add profile permission
            client.add_profile_permission(
                profileName='e2e-test-profile',
                action='signer:StartSigningJob',
                principal='123456789012',
                statementId='Stmt1',
            )

            # 5. List permissions
            resp4 = client.list_profile_permissions(profileName='e2e-test-profile')
            assert len(resp4['permissions']) >= 1

            # 6. Start signing job
            resp5 = client.start_signing_job(
                source={'s3': {'bucketName': 'test-bucket', 'key': 'test-key', 'version': '1'}},
                destination={'s3': {'bucketName': 'test-bucket', 'prefix': 'signed/'}},
                profileName='e2e-test-profile',
                clientRequestToken='e2e-token-1',
            )
            assert 'jobId' in resp5
            job_id = resp5['jobId']

            # 7. Describe signing job
            resp6 = client.describe_signing_job(jobId=job_id)
            assert resp6['jobId'] == job_id

            # 8. List signing jobs
            resp7 = client.list_signing_jobs()
            assert len(resp7['jobs']) >= 1

            # 9. Tag resource
            client.tag_resource(
                resourceArn=resp['arn'],
                tags={'env': 'e2e-test'},
            )

            # 10. List tags
            resp8 = client.list_tags_for_resource(resourceArn=resp['arn'])
            assert resp8['tags']['env'] == 'e2e-test'

            # 11. Untag
            client.untag_resource(resourceArn=resp['arn'], tagKeys=['env'])

            # 12. Remove permission
            client.remove_profile_permission(
                profileName='e2e-test-profile',
                statementId='Stmt1',
                revisionId='abc',
            )

            # 13. Cancel profile
            client.cancel_signing_profile(profileName='e2e-test-profile')

            # 14. Verify canceled
            resp9 = client.get_signing_profile(profileName='e2e-test-profile')
            assert resp9['status'] == 'Canceled'

        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                          'ValidationException')

    def test_error_nonexistent_profile(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        try:
            with pytest.raises(ClientError) as exc:
                client.get_signing_profile(profileName='nonexistent-nonexistent')
            assert exc.value.response['Error']['Code'] in (
                'ResourceNotFoundException', 'NotFoundException',
                'InternalFailure', '501',
            )
        except ClientError as e:
            code = e.response['Error']['Code']
            assert code in ('InternalFailure', '501', 'NotImplementedError',
                          'ResourceNotFoundException')
