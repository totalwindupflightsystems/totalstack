"""E2E test for Amazon FSx — boto3 against running localstack."""
import os
import pytest
import boto3
from botocore.exceptions import ClientError

ENDPOINT = os.environ.get("LOCALSTACK_ENDPOINT", "http://localhost:4566")
TEST_CREDS = {"aws_access_key_id": "test", "aws_secret_access_key": "test"}

# Check if LocalStack is running
try:
    import urllib.request
    urllib.request.urlopen(f"{ENDPOINT}/_localstack/health", timeout=2)
    LS_RUNNING = True
except Exception:
    LS_RUNNING = False


class TestFSxE2E:
    @pytest.fixture
    def client(self):
        return boto3.client("fsx", endpoint_url=ENDPOINT,
                            region_name="us-east-1", **TEST_CREDS)

    @pytest.fixture(autouse=True)
    def cleanup(self, client):
        yield
        if not LS_RUNNING:
            return
        try:
            resp = client.describe_file_systems()
            for fs in resp.get("FileSystems", []):
                try:
                    client.delete_file_system(FileSystemId=fs["FileSystemId"])
                except ClientError:
                    pass
        except ClientError:
            pass

    def test_create_describe_delete_file_system(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        # Create
        resp = client.create_file_system(
            FileSystemType="WINDOWS",
            SubnetIds=["subnet-abc123"],
            StorageCapacity=2000,
        )
        assert resp is not None
        fs_id = resp["FileSystem"]["FileSystemId"]
        assert fs_id.startswith("fs-")

        # Describe
        resp = client.describe_file_systems(FileSystemIds=[fs_id])
        assert len(resp["FileSystems"]) == 1
        assert resp["FileSystems"][0]["FileSystemId"] == fs_id

        # Delete
        client.delete_file_system(FileSystemId=fs_id)

        # Verify deleted
        with pytest.raises(ClientError) as exc:
            client.describe_file_systems(FileSystemIds=[fs_id])
        assert exc.value.response["Error"]["Code"] in (
            "FileSystemNotFound", "ResourceNotFound", "500")

    def test_create_describe_delete_backup(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        # First create a file system
        fs_resp = client.create_file_system(
            FileSystemType="WINDOWS",
            SubnetIds=["subnet-abc123"],
            StorageCapacity=2000,
        )
        fs_id = fs_resp["FileSystem"]["FileSystemId"]

        # Create backup
        resp = client.create_backup(FileSystemId=fs_id)
        assert resp is not None
        backup_id = resp["Backup"]["BackupId"]
        assert backup_id.startswith("backup-")

        # Describe backups
        resp = client.describe_backups(BackupIds=[backup_id])
        assert len(resp["Backups"]) == 1

        # Delete backup
        client.delete_backup(BackupId=backup_id)

        # Cleanup file system
        client.delete_file_system(FileSystemId=fs_id)

    def test_nonexistent_file_system(self, client):
        if not LS_RUNNING:
            pytest.skip("LocalStack not running")
        with pytest.raises(ClientError) as exc:
            client.describe_file_systems(FileSystemIds=["fs-nonexistent"])
        code = exc.value.response["Error"]["Code"]
        assert code in ("FileSystemNotFound", "ResourceNotFound",
                        "500", "InternalFailure")
