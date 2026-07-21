"""Integration test for Amazon FSx — real store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "fsx")

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(SERVICE_DIR, "models.code.py"))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

FSxStore = models_mod.FSxStore
FileSystemRecord = models_mod.FileSystemRecord
BackupRecord = models_mod.BackupRecord
VolumeRecord = models_mod.VolumeRecord
SnapshotRecord = models_mod.SnapshotRecord
StorageVirtualMachineRecord = models_mod.StorageVirtualMachineRecord
FileCacheRecord = models_mod.FileCacheRecord
FileSystemNotFound = models_mod.FileSystemNotFound
BackupNotFound = models_mod.BackupNotFound
VolumeNotFound = models_mod.VolumeNotFound
SnapshotNotFound = models_mod.SnapshotNotFound
StorageVirtualMachineNotFound = models_mod.StorageVirtualMachineNotFound
FileCacheNotFound = models_mod.FileCacheNotFound
BadRequest = models_mod.BadRequest
ResourceNotFound = models_mod.ResourceNotFound

RECORD_CLASSES = {
    "FileSystemRecord": FileSystemRecord,
    "BackupRecord": BackupRecord,
    "VolumeRecord": VolumeRecord,
    "SnapshotRecord": SnapshotRecord,
    "StorageVirtualMachineRecord": StorageVirtualMachineRecord,
    "FileCacheRecord": FileCacheRecord,
}


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file and return the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.BadRequest = BadRequest  # type: ignore[attr-defined]
    mod.FileSystemNotFound = FileSystemNotFound  # type: ignore[attr-defined]
    mod.BackupNotFound = BackupNotFound  # type: ignore[attr-defined]
    mod.VolumeNotFound = VolumeNotFound  # type: ignore[attr-defined]
    mod.SnapshotNotFound = SnapshotNotFound  # type: ignore[attr-defined]
    mod.StorageVirtualMachineNotFound = StorageVirtualMachineNotFound  # type: ignore[attr-defined]
    mod.FileCacheNotFound = FileCacheNotFound  # type: ignore[attr-defined]
    mod.ResourceNotFound = ResourceNotFound  # type: ignore[attr-defined]
    # Inject record classes
    for name, cls in RECORD_CLASSES.items():
        setattr(mod, name, cls)
    # Inject helpers
    mod._find_by_arn = None  # will be set after loading helpers
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Find the handler function
    skip_names = {"dataclass", "time", "uuid", "<lambda>", "_find_by_arn"}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith("_")
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


def _load_helpers():
    """Load _helpers.code.py and return the _find_by_arn function."""
    path = os.path.join(SERVICE_DIR, "_helpers.code.py")
    spec = importlib.util.spec_from_file_location("_helpers", path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFound = ResourceNotFound
    spec.loader.exec_module(mod)
    return mod._find_by_arn


class TestFileSystem:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FSxStore()
        return self._store

    def test_create_happy(self):
        handler = _load_handler("create-file-system")
        resp = handler(self.store, {
            "FileSystemType": "WINDOWS",
            "SubnetIds": ["subnet-abc123"],
            "StorageCapacity": 2000,
            "Tags": [{"Key": "env", "Value": "test"}],
        })
        assert resp["FileSystemId"].startswith("fs-")
        assert resp["FileSystemType"] == "WINDOWS"
        fs_tags = {t["Key"]: t["Value"] for t in resp["Tags"]}
        assert fs_tags["env"] == "test"

    def test_create_missing_required(self):
        handler = _load_handler("create-file-system")
        with pytest.raises(BadRequest):
            handler(self.store, {})

    def test_create_duplicate(self):
        handler = _load_handler("create-file-system")
        resp1 = handler(self.store, {"FileSystemType": "WINDOWS", "SubnetIds": ["subnet-1"]})
        resp2 = handler(self.store, {"FileSystemType": "WINDOWS", "SubnetIds": ["subnet-2"]})
        assert resp1["FileSystemId"] != resp2["FileSystemId"]

    def test_describe_all(self):
        handler = _load_handler("create-file-system")
        handler(self.store, {"FileSystemType": "LUSTRE", "SubnetIds": ["subnet-1"]})
        handler(self.store, {"FileSystemType": "ONTAP", "SubnetIds": ["subnet-2"]})
        desc = _load_handler("describe-file-systems")
        resp = desc(self.store, {})
        assert len(resp["FileSystems"]) == 2

    def test_describe_by_id(self):
        handler = _load_handler("create-file-system")
        r = handler(self.store, {"FileSystemType": "OPENZFS", "SubnetIds": ["subnet-1"]})
        desc = _load_handler("describe-file-systems")
        resp = desc(self.store, {"FileSystemIds": [r["FileSystemId"]]})
        assert len(resp["FileSystems"]) == 1
        assert resp["FileSystems"][0]["FileSystemId"] == r["FileSystemId"]

    def test_describe_nonexistent_ignored(self):
        desc = _load_handler("describe-file-systems")
        resp = desc(self.store, {"FileSystemIds": ["fs-nonexistent"]})
        assert resp["FileSystems"] == []

    def test_update(self):
        handler = _load_handler("create-file-system")
        r = handler(self.store, {"FileSystemType": "WINDOWS", "SubnetIds": ["subnet-1"]})
        upd = _load_handler("update-file-system")
        resp = upd(self.store, {
            "FileSystemId": r["FileSystemId"],
            "StorageCapacity": 4000,
        })
        assert resp["StorageCapacity"] == 4000

    def test_delete_happy(self):
        handler = _load_handler("create-file-system")
        r = handler(self.store, {"FileSystemType": "WINDOWS", "SubnetIds": ["subnet-1"]})
        delete = _load_handler("delete-file-system")
        delete(self.store, {"FileSystemId": r["FileSystemId"]})
        with pytest.raises(FileSystemNotFound):
            self.store.get_file_system(r["FileSystemId"])

    def test_delete_nonexistent(self):
        handler = _load_handler("delete-file-system")
        with pytest.raises(FileSystemNotFound):
            handler(self.store, {"FileSystemId": "fs-nonexistent"})


class TestBackup:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FSxStore()
        return self._store

    def _create_fs(self):
        handler = _load_handler("create-file-system")
        return handler(self.store, {
            "FileSystemType": "WINDOWS",
            "SubnetIds": ["subnet-1"],
        })

    def test_create_happy(self):
        fs = self._create_fs()
        handler = _load_handler("create-backup")
        resp = handler(self.store, {"FileSystemId": fs["FileSystemId"]})
        assert resp["BackupId"].startswith("backup-")
        assert resp["Lifecycle"] == "AVAILABLE"

    def test_create_missing_source(self):
        handler = _load_handler("create-backup")
        resp = handler(self.store, {})
        assert resp["BackupId"].startswith("backup-")

    def test_describe_all(self):
        fs = self._create_fs()
        handler = _load_handler("create-backup")
        handler(self.store, {"FileSystemId": fs["FileSystemId"]})
        handler(self.store, {"FileSystemId": fs["FileSystemId"]})
        desc = _load_handler("describe-backups")
        resp = desc(self.store, {})
        assert len(resp["Backups"]) == 2

    def test_delete_happy(self):
        handler = _load_handler("create-backup")
        r = handler(self.store, {})
        delete = _load_handler("delete-backup")
        delete(self.store, {"BackupId": r["BackupId"]})
        with pytest.raises(BackupNotFound):
            self.store.get_backup(r["BackupId"])

    def test_delete_nonexistent(self):
        handler = _load_handler("delete-backup")
        with pytest.raises(BackupNotFound):
            handler(self.store, {"BackupId": "backup-nonexistent"})


class TestVolume:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FSxStore()
        return self._store

    def test_create_happy(self):
        handler = _load_handler("create-volume")
        resp = handler(self.store, {
            "VolumeType": "ONTAP",
            "Name": "test-vol",
            "Tags": [{"Key": "env", "Value": "prod"}],
        })
        assert resp["VolumeId"].startswith("fsvol-")
        assert resp["Name"] == "test-vol"
        vol_tags = {t["Key"]: t["Value"] for t in resp["Tags"]}
        assert vol_tags["env"] == "prod"

    def test_create_missing_required(self):
        handler = _load_handler("create-volume")
        with pytest.raises(BadRequest):
            handler(self.store, {})

    def test_describe_all(self):
        handler = _load_handler("create-volume")
        handler(self.store, {"VolumeType": "ONTAP", "Name": "v1"})
        handler(self.store, {"VolumeType": "OPENZFS", "Name": "v2"})
        desc = _load_handler("describe-volumes")
        resp = desc(self.store, {})
        assert len(resp["Volumes"]) == 2

    def test_describe_nonexistent(self):
        desc = _load_handler("describe-volumes")
        resp = desc(self.store, {"VolumeIds": ["fsvol-nonexistent"]})
        assert resp["Volumes"] == []

    def test_update(self):
        handler = _load_handler("create-volume")
        r = handler(self.store, {"VolumeType": "ONTAP", "Name": "old-name"})
        upd = _load_handler("update-volume")
        resp = upd(self.store, {"VolumeId": r["VolumeId"], "Name": "new-name"})
        assert resp["Name"] == "new-name"

    def test_delete_happy(self):
        handler = _load_handler("create-volume")
        r = handler(self.store, {"VolumeType": "ONTAP", "Name": "v1"})
        delete = _load_handler("delete-volume")
        delete(self.store, {"VolumeId": r["VolumeId"]})
        with pytest.raises(VolumeNotFound):
            self.store.get_volume(r["VolumeId"])

    def test_delete_nonexistent(self):
        handler = _load_handler("delete-volume")
        with pytest.raises(VolumeNotFound):
            handler(self.store, {"VolumeId": "fsvol-nonexistent"})


class TestSnapshot:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FSxStore()
        return self._store

    def _create_vol(self):
        handler = _load_handler("create-volume")
        return handler(self.store, {"VolumeType": "ONTAP", "Name": "test-vol"})

    def test_create_happy(self):
        vol = self._create_vol()
        handler = _load_handler("create-snapshot")
        resp = handler(self.store, {"Name": "snap1", "VolumeId": vol["VolumeId"]})
        assert resp["SnapshotId"].startswith("fssnap-")
        assert resp["Name"] == "snap1"

    def test_create_missing_required(self):
        handler = _load_handler("create-snapshot")
        with pytest.raises(BadRequest):
            handler(self.store, {})

    def test_describe_all(self):
        vol = self._create_vol()
        handler = _load_handler("create-snapshot")
        handler(self.store, {"Name": "s1", "VolumeId": vol["VolumeId"]})
        handler(self.store, {"Name": "s2", "VolumeId": vol["VolumeId"]})
        desc = _load_handler("describe-snapshots")
        resp = desc(self.store, {})
        assert len(resp["Snapshots"]) == 2

    def test_update_happy(self):
        vol = self._create_vol()
        handler = _load_handler("create-snapshot")
        r = handler(self.store, {"Name": "old", "VolumeId": vol["VolumeId"]})
        upd = _load_handler("update-snapshot")
        resp = upd(self.store, {"SnapshotId": r["SnapshotId"], "Name": "new"})
        assert resp["Name"] == "new"

    def test_delete_happy(self):
        vol = self._create_vol()
        handler = _load_handler("create-snapshot")
        r = handler(self.store, {"Name": "s1", "VolumeId": vol["VolumeId"]})
        delete = _load_handler("delete-snapshot")
        delete(self.store, {"SnapshotId": r["SnapshotId"]})
        with pytest.raises(SnapshotNotFound):
            self.store.get_snapshot(r["SnapshotId"])


class TestStorageVirtualMachine:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FSxStore()
        return self._store

    def _create_fs(self):
        handler = _load_handler("create-file-system")
        return handler(self.store, {
            "FileSystemType": "ONTAP",
            "SubnetIds": ["subnet-1"],
        })

    def test_create_happy(self):
        fs = self._create_fs()
        handler = _load_handler("create-storage-virtual-machine")
        resp = handler(self.store, {
            "FileSystemId": fs["FileSystemId"],
            "Name": "svm-test",
        })
        assert resp["StorageVirtualMachineId"].startswith("svm-")
        assert resp["Name"] == "svm-test"

    def test_create_missing_required(self):
        handler = _load_handler("create-storage-virtual-machine")
        with pytest.raises(BadRequest):
            handler(self.store, {})

    def test_describe_all(self):
        fs = self._create_fs()
        handler = _load_handler("create-storage-virtual-machine")
        handler(self.store, {"FileSystemId": fs["FileSystemId"], "Name": "svm1"})
        handler(self.store, {"FileSystemId": fs["FileSystemId"], "Name": "svm2"})
        desc = _load_handler("describe-storage-virtual-machines")
        resp = desc(self.store, {})
        assert len(resp["StorageVirtualMachines"]) == 2

    def test_update(self):
        fs = self._create_fs()
        handler = _load_handler("create-storage-virtual-machine")
        r = handler(self.store, {"FileSystemId": fs["FileSystemId"], "Name": "old"})
        upd = _load_handler("update-storage-virtual-machine")
        resp = upd(self.store, {
            "StorageVirtualMachineId": r["StorageVirtualMachineId"],
            "SvmAdminPassword": "newpass",
        })
        assert resp["SvmAdminPassword"] == "newpass"

    def test_delete_happy(self):
        fs = self._create_fs()
        handler = _load_handler("create-storage-virtual-machine")
        r = handler(self.store, {"FileSystemId": fs["FileSystemId"], "Name": "svm1"})
        delete = _load_handler("delete-storage-virtual-machine")
        delete(self.store, {"StorageVirtualMachineId": r["StorageVirtualMachineId"]})
        with pytest.raises(StorageVirtualMachineNotFound):
            self.store.get_storage_virtual_machine(r["StorageVirtualMachineId"])


class TestFileCache:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = FSxStore()
        return self._store

    def test_create_happy(self):
        handler = _load_handler("create-file-cache")
        resp = handler(self.store, {
            "FileCacheType": "LUSTRE",
            "FileCacheTypeVersion": "2.12",
            "StorageCapacity": 1200,
            "SubnetIds": ["subnet-1"],
        })
        assert resp["FileCacheId"].startswith("fc-")
        assert resp["FileCacheType"] == "LUSTRE"

    def test_create_missing_required(self):
        handler = _load_handler("create-file-cache")
        with pytest.raises(BadRequest):
            handler(self.store, {})

    def test_describe_all(self):
        handler = _load_handler("create-file-cache")
        handler(self.store, {
            "FileCacheType": "LUSTRE", "FileCacheTypeVersion": "2.12",
            "StorageCapacity": 1200, "SubnetIds": ["subnet-1"],
        })
        handler(self.store, {
            "FileCacheType": "LUSTRE", "FileCacheTypeVersion": "2.12",
            "StorageCapacity": 2400, "SubnetIds": ["subnet-2"],
        })
        desc = _load_handler("describe-file-caches")
        resp = desc(self.store, {})
        assert len(resp["FileCaches"]) == 2

    def test_update(self):
        handler = _load_handler("create-file-cache")
        r = handler(self.store, {
            "FileCacheType": "LUSTRE", "FileCacheTypeVersion": "2.12",
            "StorageCapacity": 1200, "SubnetIds": ["subnet-1"],
        })
        upd = _load_handler("update-file-cache")
        resp = upd(self.store, {
            "FileCacheId": r["FileCacheId"],
            "LustreConfiguration": {"DeploymentType": "CACHE_1"},
        })
        assert resp["LustreConfiguration"] == {"DeploymentType": "CACHE_1"}

    def test_delete_happy(self):
        handler = _load_handler("create-file-cache")
        r = handler(self.store, {
            "FileCacheType": "LUSTRE", "FileCacheTypeVersion": "2.12",
            "StorageCapacity": 1200, "SubnetIds": ["subnet-1"],
        })
        delete = _load_handler("delete-file-cache")
        delete(self.store, {"FileCacheId": r["FileCacheId"]})
        with pytest.raises(FileCacheNotFound):
            self.store.get_file_cache(r["FileCacheId"])
