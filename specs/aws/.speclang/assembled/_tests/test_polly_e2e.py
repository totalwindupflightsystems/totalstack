"""E2E test for Polly — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

# Check if localstack is running
LS_RUNNING = False
try:
    import urllib.request
    urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
    LS_RUNNING = True
except Exception:
    pass


class TestPollyE2E:
    @pytest.fixture
    def client(self):
        return boto3.client('polly', endpoint_url=ENDPOINT,
                            region_name='us-east-1', **TEST_CREDS)

    def test_describe_voices(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        response = client.describe_voices()
        assert "Voices" in response
        assert isinstance(response["Voices"], list)

    def test_synthesize_speech_full_workflow(self, client):
        """Synthesize speech → verify audio returned."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        response = client.synthesize_speech(
            OutputFormat='mp3',
            Text='Hello world from TotalStack Polly!',
            VoiceId='Joanna',
        )
        assert response is not None
        assert "AudioStream" in response
        assert "ContentType" in response
        assert response["ContentType"] == "audio/mpeg"

    def test_lexicon_crud_workflow(self, client):
        """Put lexicon → Get → List → Delete → verify deleted."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        # Put
        client.put_lexicon(
            Name='e2e-test-lexicon',
            Content='<lexicon><lexeme><grapheme>test</grapheme></lexeme></lexicon>',
        )
        # Get
        response = client.get_lexicon(Name='e2e-test-lexicon')
        assert response["Lexicon"]["Name"] == 'e2e-test-lexicon'
        assert "LexiconAttributes" in response
        # List
        response = client.list_lexicons()
        assert len(response["Lexicons"]) >= 1
        # Delete
        client.delete_lexicon(Name='e2e-test-lexicon')
        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_lexicon(Name='e2e-test-lexicon')
        assert exc.value.response['Error']['Code'] == 'LexiconNotFoundException'

    def test_error_nonexistent_lexicon(self, client):
        """Reading nonexistent lexicon fails."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        with pytest.raises(ClientError) as exc:
            client.get_lexicon(Name='nonexistent-lexicon')
        assert exc.value.response['Error']['Code'] == 'LexiconNotFoundException'

    def test_speech_synthesis_task_workflow(self, client):
        """Start task → get task → list tasks."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        # Start
        response = client.start_speech_synthesis_task(
            OutputFormat='mp3',
            OutputS3BucketName='test-bucket',
            Text='Async task test',
            VoiceId='Joanna',
        )
        assert "SynthesisTask" in response
        task_id = response["SynthesisTask"]["TaskId"]
        assert task_id is not None
        # Get
        response = client.get_speech_synthesis_task(TaskId=task_id)
        assert response["SynthesisTask"]["TaskId"] == task_id
        assert response["SynthesisTask"]["TaskStatus"] == "completed"
        # List
        response = client.list_speech_synthesis_tasks()
        assert len(response["SynthesisTasks"]) >= 1

    def test_error_nonexistent_task(self, client):
        """Reading nonexistent task fails."""
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        with pytest.raises(ClientError) as exc:
            client.get_speech_synthesis_task(TaskId='00000000-0000-0000-0000-000000000000')
        assert exc.value.response['Error']['Code'] in (
            'SynthesisTaskNotFoundException', 'InvalidTaskIdException')
