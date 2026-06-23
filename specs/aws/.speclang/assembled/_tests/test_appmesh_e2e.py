"""E2E tests for App Mesh — boto3 against running localstack.

These tests require a running LocalStack instance with App Mesh provider.
They use pytest.mark.skipif to skip gracefully when LocalStack is not running.
"""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get('LOCALSTACK_ENDPOINT', 'http://localhost:4566')
TEST_CREDS = {'aws_access_key_id': 'test', 'aws_secret_access_key': 'test'}

# Check if LocalStack is reachable
def _is_localstack_running():
    try:
        import urllib.request
        urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
        return True
    except Exception:
        return False

LS_RUNNING = _is_localstack_running()


class TestAppMeshE2E:
    """End-to-end tests using boto3 against running localstack."""

    @pytest.fixture
    def client(self):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        return boto3.client('appmesh', endpoint_url=ENDPOINT,
                           region_name='us-east-1', **TEST_CREDS)

    def test_full_mesh_crud_workflow(self, client):
        """Create mesh → describe → list → update → delete → verify deleted."""
        # 1. Create mesh
        resp = client.create_mesh(meshName='e2e-mesh')
        assert resp is not None
        assert resp['mesh']['meshName'] == 'e2e-mesh'
        assert resp['mesh']['status']['status'] == 'ACTIVE'

        # 2. Describe mesh
        resp = client.describe_mesh(meshName='e2e-mesh')
        assert resp['mesh']['meshName'] == 'e2e-mesh'

        # 3. List meshes
        resp = client.list_meshes()
        assert len(resp['meshes']) >= 1

        # 4. Update mesh
        resp = client.update_mesh(
            meshName='e2e-mesh',
            spec={'egressFilter': {'type': 'ALLOW_ALL'}}
        )
        assert resp['mesh']['spec']['egressFilter']['type'] == 'ALLOW_ALL'

        # 5. Delete mesh
        client.delete_mesh(meshName='e2e-mesh')

        # 6. Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_mesh(meshName='e2e-mesh')
        assert exc.value.response['Error']['Code'] == 'NotFoundException'

    def test_full_virtual_node_workflow(self, client):
        """Create mesh + virtual node → describe → list → delete."""
        # Setup: create parent mesh
        client.create_mesh(meshName='e2e-vn-mesh')

        # 1. Create virtual node
        resp = client.create_virtual_node(
            meshName='e2e-vn-mesh',
            virtualNodeName='e2e-vn',
            spec={'backends': []}
        )
        assert resp['virtualNode']['virtualNodeName'] == 'e2e-vn'

        # 2. Describe
        resp = client.describe_virtual_node(
            meshName='e2e-vn-mesh',
            virtualNodeName='e2e-vn'
        )
        assert resp['virtualNode']['virtualNodeName'] == 'e2e-vn'

        # 3. List
        resp = client.list_virtual_nodes(meshName='e2e-vn-mesh')
        assert len(resp['virtualNodes']) >= 1

        # 4. Update
        resp = client.update_virtual_node(
            meshName='e2e-vn-mesh',
            virtualNodeName='e2e-vn',
            spec={'backends': [{'virtualService': {'virtualServiceName': 'test.local'}}]}
        )
        assert resp['virtualNode']['spec']['backends'][0]['virtualService']['virtualServiceName'] == 'test.local'

        # 5. Delete
        client.delete_virtual_node(
            meshName='e2e-vn-mesh',
            virtualNodeName='e2e-vn'
        )
        with pytest.raises(ClientError) as exc:
            client.describe_virtual_node(
                meshName='e2e-vn-mesh',
                virtualNodeName='e2e-vn'
            )
        assert exc.value.response['Error']['Code'] == 'NotFoundException'

        # Cleanup
        client.delete_mesh(meshName='e2e-vn-mesh')

    def test_error_nonexistent_mesh(self, client):
        """Describe nonexistent mesh raises NotFoundException."""
        with pytest.raises(ClientError) as exc:
            client.describe_mesh(meshName='no-such-mesh-e2e')
        assert exc.value.response['Error']['Code'] == 'NotFoundException'

    def test_error_duplicate_mesh(self, client):
        """Create duplicate mesh raises ConflictException."""
        client.create_mesh(meshName='e2e-dup-mesh')
        try:
            with pytest.raises(ClientError) as exc:
                client.create_mesh(meshName='e2e-dup-mesh')
            assert 'Conflict' in exc.value.response['Error']['Code'] or \
                   'AlreadyExists' in exc.value.response['Error']['Code'] or \
                   exc.value.response['Error']['Code'] == 'ConflictException'
        finally:
            client.delete_mesh(meshName='e2e-dup-mesh')
