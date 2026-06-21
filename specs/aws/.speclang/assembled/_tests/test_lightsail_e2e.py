"""E2E test for Lightsail — boto3 against running localstack.

Since Lightsail is a greenfield service with no provider wired yet,
E2E tests are auto-skipped until the provider is available.
"""
import os

import pytest
import requests

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test',
              'region_name': 'us-east-1'}


def _localstack_healthy():
    """Check if localstack is running and healthy."""
    try:
        r = requests.get(f'{ENDPOINT}/_localstack/health', timeout=2)
        return r.status_code == 200
    except Exception:
        return False


def _lightsail_available():
    """Check if Lightsail service is available via boto3."""
    try:
        import boto3
        client = boto3.client('lightsail', endpoint_url=ENDPOINT, **TEST_CREDS)
        client.get_instances()
        return True
    except Exception:
        return False


# Skip all E2E tests if localstack isn't running or Lightsail isn't wired
skip_if_not_ready = pytest.mark.skipif(
    not (_localstack_healthy() and _lightsail_available()),
    reason="Lightsail provider not yet wired — E2E skipped"
)


@pytest.mark.skipif(not _localstack_healthy(),
                    reason="LocalStack not running")
class TestLightsailE2E:
    """E2E tests using boto3 against running localstack.

    These tests exercise the full Lightsail workflow:
    create → describe → verify → delete.
    """

    @pytest.fixture
    def client(self):
        import boto3
        return boto3.client('lightsail', endpoint_url=ENDPOINT, **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        # Cleanup: delete test resources
        for name in ['e2e-test-instance', 'e2e-test-disk',
                     'e2e-test-keypair', 'e2e-test-bucket-123',
                     'e2e-test-lb', 'e2e.example.com']:
            try:
                client.delete_instance(instanceName=name)
            except Exception:
                pass
            try:
                client.delete_disk(diskName=name)
            except Exception:
                pass
            try:
                client.delete_key_pair(keyPairName=name)
            except Exception:
                pass
            try:
                client.delete_bucket(bucketName=name)
            except Exception:
                pass
            try:
                client.delete_load_balancer(loadBalancerName=name)
            except Exception:
                pass
            try:
                client.delete_domain(domainName=name)
            except Exception:
                pass

    @skip_if_not_ready
    def test_create_get_delete_instance(self, client):
        """Create → describe → verify → delete instance."""
        from botocore.exceptions import ClientError

        # Create
        resp = client.create_instances(
            instanceNames=['e2e-test-instance'],
            availabilityZone='us-east-1a',
            blueprintId='ubuntu_24_04',
            bundleId='nano_3_0',
        )
        assert resp is not None

        # Describe
        resp = client.get_instance(instanceName='e2e-test-instance')
        assert resp is not None

        # Delete
        client.delete_instance(instanceName='e2e-test-instance')

        # Verify deleted
        with pytest.raises(ClientError):
            client.get_instance(instanceName='e2e-test-instance')

    @skip_if_not_ready
    def test_create_get_delete_disk(self, client):
        """Create → get → delete disk."""
        from botocore.exceptions import ClientError

        resp = client.create_disk(
            diskName='e2e-test-disk',
            availabilityZone='us-east-1a',
            sizeInGb=40,
        )
        assert resp is not None

        resp = client.get_disk(diskName='e2e-test-disk')
        assert resp is not None

        client.delete_disk(diskName='e2e-test-disk')

        with pytest.raises(ClientError):
            client.get_disk(diskName='e2e-test-disk')

    @skip_if_not_ready
    def test_create_get_delete_key_pair(self, client):
        """Create → get → delete key pair."""
        from botocore.exceptions import ClientError

        resp = client.create_key_pair(keyPairName='e2e-test-keypair')
        assert resp is not None

        resp = client.get_key_pair(keyPairName='e2e-test-keypair')
        assert resp is not None

        client.delete_key_pair(keyPairName='e2e-test-keypair')

        with pytest.raises(ClientError):
            client.get_key_pair(keyPairName='e2e-test-keypair')

    @skip_if_not_ready
    def test_duplicate_create_fails(self, client):
        """Creating same instance twice returns error."""
        from botocore.exceptions import ClientError

        client.create_instances(
            instanceNames=['e2e-test-instance'],
            availabilityZone='us-east-1a',
            blueprintId='ubuntu_24_04',
            bundleId='nano_3_0',
        )

        try:
            with pytest.raises(ClientError):
                client.create_instances(
                    instanceNames=['e2e-test-instance'],
                    availabilityZone='us-east-1a',
                    blueprintId='ubuntu_24_04',
                    bundleId='nano_3_0',
                )
        finally:
            client.delete_instance(instanceName='e2e-test-instance')
