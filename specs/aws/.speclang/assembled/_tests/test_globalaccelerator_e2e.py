"""E2E test for GlobalAccelerator — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}
LS_RUNNING = False

# Check if LocalStack is running
try:
    import urllib.request
    resp = urllib.request.urlopen(f'{ENDPOINT}/_localstack/health', timeout=2)
    LS_RUNNING = True
except Exception:
    pass


class TestGlobalAcceleratorE2E:

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('globalaccelerator', endpoint_url=ENDPOINT,
                           region_name='us-west-2', **TEST_CREDS)

    def test_full_crud_workflow(self, client):
        """Create accelerator → describe → list → update → delete."""

        # 1. Create accelerator
        resp = client.create_accelerator(
            Name='e2e-test-ga',
            IdempotencyToken='e2e-token-1',
            Enabled=True,
        )
        assert resp is not None
        assert 'Accelerator' in resp
        accel_arn = resp['Accelerator']['AcceleratorArn']
        assert resp['Accelerator']['Name'] == 'e2e-test-ga'

        # 2. Describe
        resp = client.describe_accelerator(AcceleratorArn=accel_arn)
        assert resp['Accelerator']['Name'] == 'e2e-test-ga'

        # 3. List
        resp = client.list_accelerators()
        assert len(resp['Accelerators']) >= 1

        # 4. Update
        resp = client.update_accelerator(
            AcceleratorArn=accel_arn,
            Enabled=False,
        )
        assert resp['Accelerator']['Enabled'] is False

        # 5. Delete
        client.delete_accelerator(AcceleratorArn=accel_arn)

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_accelerator(AcceleratorArn=accel_arn)
        assert 'AcceleratorNotFoundException' in str(exc.value)

    def test_listener_workflow(self, client):
        """Create accelerator → create listener → describe → update → delete"""
        resp = client.create_accelerator(
            Name='e2e-listener-ga',
            IdempotencyToken='e2e-lis-1',
            Enabled=True,
        )
        accel_arn = resp['Accelerator']['AcceleratorArn']

        # Create listener
        resp = client.create_listener(
            AcceleratorArn=accel_arn,
            PortRanges=[{'FromPort': 80, 'ToPort': 80}],
            Protocol='TCP',
            IdempotencyToken='e2e-lis-2',
        )
        listener_arn = resp['Listener']['ListenerArn']
        assert resp['Listener']['Protocol'] == 'TCP'

        # Describe
        resp = client.describe_listener(ListenerArn=listener_arn)
        assert resp['Listener']['Protocol'] == 'TCP'

        # Update protocol
        resp = client.update_listener(
            ListenerArn=listener_arn,
            Protocol='UDP',
        )
        assert resp['Listener']['Protocol'] == 'UDP'

        # Delete listener
        client.delete_listener(ListenerArn=listener_arn)
        with pytest.raises(ClientError) as exc:
            client.describe_listener(ListenerArn=listener_arn)
        assert 'ListenerNotFoundException' in str(exc.value)

        # Clean up accelerator
        client.delete_accelerator(AcceleratorArn=accel_arn)

    def test_tag_workflow(self, client):
        """Tag → list tags → untag → verify"""
        resp = client.create_accelerator(
            Name='e2e-tags-ga',
            IdempotencyToken='e2e-tag-1',
            Enabled=True,
            Tags=[{'Key': 'env', 'Value': 'e2e'}],
        )
        accel_arn = resp['Accelerator']['AcceleratorArn']

        # Add another tag
        client.tag_resource(
            ResourceArn=accel_arn,
            Tags=[{'Key': 'team', 'Value': 'test'}],
        )

        # List tags
        resp = client.list_tags_for_resource(ResourceArn=accel_arn)
        tags = {t['Key']: t['Value'] for t in resp['Tags']}
        assert tags.get('env') == 'e2e'
        assert tags.get('team') == 'test'

        # Untag
        client.untag_resource(
            ResourceArn=accel_arn,
            TagKeys=['team'],
        )
        resp = client.list_tags_for_resource(ResourceArn=accel_arn)
        tags = {t['Key']: t['Value'] for t in resp['Tags']}
        assert 'team' not in tags
        assert tags['env'] == 'e2e'

        # Cleanup
        client.delete_accelerator(AcceleratorArn=accel_arn)

    def test_error_nonexistent(self, client):
        """Reading nonexistent resource fails."""
        with pytest.raises(ClientError) as exc:
            client.describe_accelerator(
                AcceleratorArn='arn:aws:globalaccelerator::000000000000:accelerator/nonexistent')
        assert 'AcceleratorNotFoundException' in str(exc.value)
