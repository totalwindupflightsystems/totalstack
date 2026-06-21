"""E2E tests for CodeArtifact — boto3 against running localstack.

NOTE: CodeArtifact is a greenfield service without a LocalStack provider.
These tests are SKIPPED until the CodeArtifact provider is wired into the localstack plugin system.
"""

import os
import pytest

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test', 'region_name': 'us-east-1'}

# Check if the codeartifact provider is available
import requests
import json

def _codeartifact_available():
    """Check if CodeArtifact service is registered in the localstack instance."""
    try:
        resp = requests.get(f"{ENDPOINT}/_localstack/health", timeout=2)
        health = resp.json()
        services = health.get("services", {})
        return "codeartifact" in services
    except Exception:
        return False

CODEARTIFACT_AVAILABLE = _codeartifact_available()
SKIP_REASON = "CodeArtifact provider not yet wired into LocalStack plugin system (greenfield service)"


class TestCodeArtifactE2E:

    @pytest.fixture
    def client(self):
        import boto3
        return boto3.client('codeartifact', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.mark.skipif(not CODEARTIFACT_AVAILABLE, reason=SKIP_REASON)
    def test_full_domain_lifecycle(self, client):
        """Create domain → describe → delete → verify."""
        # 1. Create
        resp = client.create_domain(domain='test-e2e-domain')
        assert resp is not None

        # 2. Describe
        resp = client.describe_domain(domain='test-e2e-domain')
        assert resp['domain']['name'] == 'test-e2e-domain'
        assert resp['domain']['status'] == 'Active'

        # 3. Delete
        client.delete_domain(domain='test-e2e-domain')

        # 4. Verify deleted
        with pytest.raises(Exception):
            client.describe_domain(domain='test-e2e-domain')

    @pytest.mark.skipif(not CODEARTIFACT_AVAILABLE, reason=SKIP_REASON)
    def test_repository_lifecycle(self, client):
        """Create domain → create repo → describe repo → delete repo → delete domain."""
        client.create_domain(domain='test-e2e-domain')

        # Create repository
        resp = client.create_repository(
            domain='test-e2e-domain',
            repository='test-e2e-repo',
            description='E2E test repository'
        )
        assert resp['repository']['name'] == 'test-e2e-repo'

        # Describe
        resp = client.describe_repository(domain='test-e2e-domain', repository='test-e2e-repo')
        assert resp['repository']['description'] == 'E2E test repository'

        # Delete repo
        client.delete_repository(domain='test-e2e-domain', repository='test-e2e-repo')

        # Cleanup
        client.delete_domain(domain='test-e2e-domain')

    @pytest.mark.skipif(not CODEARTIFACT_AVAILABLE, reason=SKIP_REASON)
    def test_error_duplicate_create(self, client):
        """Creating duplicate domain fails."""
        client.create_domain(domain='test-e2e-domain')
        with pytest.raises(Exception) as exc:
            client.create_domain(domain='test-e2e-domain')
        # AWS returns ConflictException
        assert 'conflict' in str(exc.value).lower() or 'already' in str(exc.value).lower()
        client.delete_domain(domain='test-e2e-domain')

    @pytest.mark.skipif(not CODEARTIFACT_AVAILABLE, reason=SKIP_REASON)
    def test_error_nonexistent_read(self, client):
        """Reading nonexistent domain fails."""
        with pytest.raises(Exception) as exc:
            client.describe_domain(domain='nonexistent-domain')
        assert 'not found' in str(exc.value).lower() or 'resource' in str(exc.value).lower()
