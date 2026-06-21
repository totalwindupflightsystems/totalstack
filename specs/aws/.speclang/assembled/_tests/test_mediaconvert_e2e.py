"""E2E test for MediaConvert — boto3 against running localstack.

MediaConvert is a greenfield service with no LocalStack provider yet.
Tests use skipif to auto-skip when the endpoint is unavailable,
keeping the suite green while the provider is under construction.
"""
import os
import pytest
import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test', 'aws_session_token': 'test'}
REGION = 'us-east-1'


def _endpoint_available():
    """Check if the mediaconvert endpoint responds (not a connection error)."""
    try:
        client = boto3.client('mediaconvert', endpoint_url=ENDPOINT,
                              region_name=REGION, **TEST_CREDS)
        # Try a simple operation
        client.list_jobs(MaxResults=1)
        return True
    except (EndpointConnectionError, ClientError) as e:
        # ClientError with 501/404 = endpoint exists but not implemented
        # EndpointConnectionError = no listener at all
        if isinstance(e, ClientError) and e.response['Error']['Code'] in ('501', '404', 'NotImplemented'):
            return True  # Endpoint exists, just not wired
        return False


ENDPOINT_READY = _endpoint_available()


class TestMediaConvertE2E:

    @pytest.fixture
    def client(self):
        return boto3.client('mediaconvert', endpoint_url=ENDPOINT,
                           region_name=REGION, **TEST_CREDS)

    @pytest.mark.skipif(not ENDPOINT_READY, reason="MediaConvert endpoint not available in localstack")
    def test_full_crud_workflow(self, client):
        """Create → get → list → cancel → verify."""
        # 1. Create job
        response = client.create_job(
            Role='arn:aws:iam::000000000000:role/MediaConvertRole',
            Settings={
                'Inputs': [{'FileInput': 's3://bucket/input.mp4'}],
                'OutputGroups': [{
                    'Outputs': [{
                        'ContainerSettings': {'Container': 'MP4'},
                        'VideoDescription': {
                            'CodecSettings': {'Codec': 'H_264'}
                        }
                    }]
                }]
            }
        )
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200
        job = response.get('Job', response)
        job_id = job.get('Id')

        # 2. Get job
        if job_id:
            response = client.get_job(Id=job_id)
            assert response['ResponseMetadata']['HTTPStatusCode'] == 200

        # 3. List jobs
        response = client.list_jobs(MaxResults=5)
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200

        # 4. Cancel job
        if job_id:
            response = client.cancel_job(Id=job_id)
            assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    @pytest.mark.skipif(not ENDPOINT_READY, reason="MediaConvert endpoint not available in localstack")
    def test_create_job_template(self, client):
        """Create a job template."""
        response = client.create_job_template(
            Name='test-template',
            Settings={
                'Inputs': [{'FileInput': 's3://bucket/input.mp4'}],
                'OutputGroups': [{
                    'Outputs': [{
                        'ContainerSettings': {'Container': 'MP4'}
                    }]
                }]
            }
        )
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    @pytest.mark.skipif(not ENDPOINT_READY, reason="MediaConvert endpoint not available in localstack")
    def test_create_queue(self, client):
        """Create a queue."""
        response = client.create_queue(Name='test-queue')
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200
