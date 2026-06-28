"""E2E test for Transcribe — boto3 against running localstack."""
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


class TestTranscribeE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('transcribe', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_vocabulary_crud_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client.create_vocabulary(
            VocabularyName='e2e-test-vocab',
            LanguageCode='en-US',
        )
        resp = client.get_vocabulary(VocabularyName='e2e-test-vocab')
        assert resp['VocabularyName'] == 'e2e-test-vocab'
        resp = client.list_vocabularies()
        assert len(resp['Vocabularies']) >= 1
        client.delete_vocabulary(VocabularyName='e2e-test-vocab')
        with pytest.raises(ClientError) as exc:
            client.get_vocabulary(VocabularyName='e2e-test-vocab')
        assert exc.value.response['Error']['Code'] == 'NotFoundException'

    def test_vocabulary_filter_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client.create_vocabulary_filter(
            VocabularyFilterName='e2e-test-filter',
            LanguageCode='en-US',
            Words=['badword'],
        )
        resp = client.get_vocabulary_filter(VocabularyFilterName='e2e-test-filter')
        assert resp['VocabularyFilterName'] == 'e2e-test-filter'
        client.delete_vocabulary_filter(VocabularyFilterName='e2e-test-filter')

    def test_transcription_job_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client.start_transcription_job(
            TranscriptionJobName='e2e-test-job',
            Media={'MediaFileUri': 's3://bucket/test.mp3'},
            LanguageCode='en-US',
        )
        resp = client.get_transcription_job(TranscriptionJobName='e2e-test-job')
        assert resp['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED'
        client.delete_transcription_job(TranscriptionJobName='e2e-test-job')

    def test_language_model_workflow(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        client.create_language_model(
            LanguageCode='en-US',
            BaseModelName='NarrowBand',
            ModelName='e2e-test-model',
            InputDataConfig={
                'S3Uri': 's3://bucket/train/',
                'TuningDataS3Uri': 's3://bucket/tune/',
                'DataAccessRoleArn': 'arn:aws:iam::123456789012:role/TranscribeRole',
            },
        )
        resp = client.describe_language_model(ModelName='e2e-test-model')
        assert resp['ModelName'] == 'e2e-test-model'
        client.delete_language_model(ModelName='e2e-test-model')

    def test_error_nonexistent(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        with pytest.raises(ClientError) as exc:
            client.get_vocabulary(VocabularyName='does-not-exist')
        assert exc.value.response['Error']['Code'] == 'NotFoundException'
