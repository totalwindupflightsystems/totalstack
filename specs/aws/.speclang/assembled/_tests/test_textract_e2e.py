"""E2E test for Textract — boto3 against running localstack."""
import os
import pytest
import json
import urllib.request
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}
REGION = 'us-east-1'


def _localstack_healthy():
    """Check if localstack is running."""
    try:
        r = urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
        return True
    except Exception:
        return False


def _textract_available():
    """Check if Textract is a registered localstack service."""
    try:
        r = urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
        h = json.loads(r.read())
        svcs = h.get('services', {})
        return 'textract' in svcs and svcs['textract'] == 'available'
    except Exception:
        return False


skip_if_no_textract = pytest.mark.skipif(
    not _textract_available(),
    reason="Textract provider not wired to localstack (greenfield service)"
)


class TestTextractE2E:

    @pytest.fixture
    def client(self):
        if not _textract_available():
            pytest.skip("Textract not available in localstack")
        return boto3.client('textract', endpoint_url=ENDPOINT,
                           region_name=REGION, **TEST_CREDS)

    @skip_if_no_textract
    @pytest.mark.skip(reason="Textract provider not yet wired — greenfield service")
    def test_detect_document_text(self, client):
        """Sync text detection — create → verify response."""
        response = client.detect_document_text(
            Document={"Bytes": "bW9ja2Jhc2U2NA=="}
        )
        assert "Blocks" in response
        assert "DocumentMetadata" in response
        assert len(response["Blocks"]) > 0

    @skip_if_no_textract
    @pytest.mark.skip(reason="Textract provider not yet wired — greenfield service")
    def test_analyze_document_tables(self, client):
        """Document analysis with TABLES feature."""
        response = client.analyze_document(
            Document={"Bytes": "bW9ja2Jhc2U2NA=="},
            FeatureTypes=["TABLES"]
        )
        block_types = [b["BlockType"] for b in response["Blocks"]]
        assert "TABLE" in block_types

    @skip_if_no_textract
    @pytest.mark.skip(reason="Textract provider not yet wired — greenfield service")
    def test_adapter_crud_workflow(self, client):
        """Create → get → delete adapter."""
        # Create
        response = client.create_adapter(
            AdapterName="e2e-test-adapter",
            FeatureTypes=["TABLES", "FORMS"],
        )
        adapter_id = response["AdapterId"]
        assert adapter_id

        # Get
        response = client.get_adapter(AdapterId=adapter_id)
        assert response["AdapterId"] == adapter_id
        assert response["AdapterName"] == "e2e-test-adapter"

        # Delete
        client.delete_adapter(AdapterId=adapter_id)

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.get_adapter(AdapterId=adapter_id)
        assert exc.value.response['Error']['Code'] == 'ResourceNotFoundException'
