"""Amazon FSx — managed file systems (Lustre, Windows, NetApp ONTAP, OpenZFS).

Provides persistent, scalable file storage backed by SSD and HDD.
Supports 4 file system types with backups, volumes, snapshots, and caches.
"""


# === Exception classes ===

class FileSystemNotFound(Exception):
    """Raised when a file system ID doesn't exist in the store."""
    pass


class BackupNotFound(Exception):
    """Raised when a backup ID doesn't exist in the store."""
    pass


class VolumeNotFound(Exception):
    """Raised when a volume ID doesn't exist in the store."""
    pass


class SnapshotNotFound(Exception):
    """Raised when a snapshot ID doesn't exist in the store."""
    pass


class StorageVirtualMachineNotFound(Exception):
    """Raised when an SVM ID doesn't exist in the store."""
    pass


class FileCacheNotFound(Exception):
    """Raised when a file cache ID doesn't exist in the store."""
    pass


class BadRequest(Exception):
    """Raised for invalid parameters or missing required fields."""
    pass


class ResourceNotFound(Exception):
    """Generic resource not found."""
    pass


class IncompatibleParameterError(Exception):
    """Raised when parameters are incompatible."""
    pass


class InternalServerError(Exception):
    """Internal server error."""
    pass


# === Helper ===

_counter = [0]

def _next_id(prefix):
    _counter[0] += 1
    return f"{prefix}-{_counter[0]:08d}"


def _convert_tags(tags):
    """Convert AWS tags list-of-dicts to flat dict."""
    if not tags:
        return {}
    if isinstance(tags, dict):
        return dict(tags)
    result = {}
    for t in tags:
        k = t.get("Key", t.get("key", ""))
        v = t.get("Value", t.get("value", ""))
        result[k] = v
    return result


def _serialize_tags(tags):
    """Convert flat dict to AWS tags list: [{'Key': k, 'Value': v}, ...]."""
    if not tags:
        return []
    if isinstance(tags, list):
        return tags
    return [{"Key": k, "Value": v} for k, v in tags.items()]


# === Record classes ===

class FileSystemRecord:
    def __init__(self, FileSystemType, SubnetIds, FileSystemId=None,
                 StorageCapacity=None, StorageType=None,
                 SecurityGroupIds=None, Tags=None, KmsKeyId=None,
                 WindowsConfiguration=None, LustreConfiguration=None,
                 OntapConfiguration=None, OpenZFSConfiguration=None,
                 FileSystemTypeVersion=None, NetworkType=None,
                 DNSName=None, OwnerId=None, CreationToken=None,
                 Lifecycle=None, **kwargs):
        self.FileSystemId = FileSystemId or _next_id("fs")
        self.FileSystemType = FileSystemType
        self.SubnetIds = SubnetIds or []
        self.StorageCapacity = StorageCapacity or 0
        self.StorageType = StorageType
        self.SecurityGroupIds = SecurityGroupIds or []
        self.Tags = _convert_tags(Tags)
        self.KmsKeyId = KmsKeyId
        self.WindowsConfiguration = WindowsConfiguration
        self.LustreConfiguration = LustreConfiguration
        self.OntapConfiguration = OntapConfiguration
        self.OpenZFSConfiguration = OpenZFSConfiguration
        self.FileSystemTypeVersion = FileSystemTypeVersion
        self.NetworkType = NetworkType
        self.DNSName = DNSName
        self.OwnerId = OwnerId
        self.CreationToken = CreationToken
        self.Lifecycle = Lifecycle or "AVAILABLE"

    def to_dict(self):
        return {
            "FileSystemId": self.FileSystemId,
            "FileSystemType": self.FileSystemType,
            "SubnetIds": self.SubnetIds,
            "StorageCapacity": self.StorageCapacity,
            "StorageType": self.StorageType,
            "SecurityGroupIds": self.SecurityGroupIds,
            "Tags": self.Tags,
            "KmsKeyId": self.KmsKeyId,
            "WindowsConfiguration": self.WindowsConfiguration,
            "LustreConfiguration": self.LustreConfiguration,
            "OntapConfiguration": self.OntapConfiguration,
            "OpenZFSConfiguration": self.OpenZFSConfiguration,
            "FileSystemTypeVersion": self.FileSystemTypeVersion,
            "NetworkType": self.NetworkType,
            "DNSName": self.DNSName,
            "OwnerId": self.OwnerId,
            "CreationToken": self.CreationToken,
            "Lifecycle": self.Lifecycle,
        }


class BackupRecord:
    def __init__(self, BackupId=None, FileSystemId=None, VolumeId=None,
                 Tags=None, Lifecycle=None, Type=None, **kwargs):
        self.BackupId = BackupId or _next_id("backup")
        self.FileSystemId = FileSystemId
        self.VolumeId = VolumeId
        self._raw_tags = Tags or []
        self.Lifecycle = Lifecycle or "AVAILABLE"
        self.Type = Type or "USER_INITIATED"
        import time
        self.CreationTime = time.time()

    def to_dict(self):
        result = {
            "BackupId": self.BackupId,
            "Lifecycle": self.Lifecycle,
            "Type": self.Type,
            "CreationTime": self.CreationTime,
            "Tags": self._raw_tags if isinstance(self._raw_tags, list) else [{"Key": k, "Value": v} for k, v in _convert_tags(self._raw_tags).items()],
            "FileSystem": {"FileSystemId": self.FileSystemId or "fs-default"},
        }
        if self.VolumeId:
            result["Volume"] = {"VolumeId": self.VolumeId}
        return result


class VolumeRecord:
    def __init__(self, VolumeType, Name, VolumeId=None,
                 OntapConfiguration=None, OpenZFSConfiguration=None,
                 Tags=None, FileSystemId=None, Lifecycle=None, **kwargs):
        self.VolumeId = VolumeId or _next_id("fsvol")
        self.VolumeType = VolumeType
        self.Name = Name
        self.OntapConfiguration = OntapConfiguration
        self.OpenZFSConfiguration = OpenZFSConfiguration
        self.Tags = _convert_tags(Tags)
        self.FileSystemId = FileSystemId
        self.Lifecycle = Lifecycle or "AVAILABLE"

    def to_dict(self):
        return {
            "VolumeId": self.VolumeId,
            "VolumeType": self.VolumeType,
            "Name": self.Name,
            "OntapConfiguration": self.OntapConfiguration,
            "OpenZFSConfiguration": self.OpenZFSConfiguration,
            "Tags": self.Tags,
            "FileSystemId": self.FileSystemId,
            "Lifecycle": self.Lifecycle,
        }


class SnapshotRecord:
    def __init__(self, Name, VolumeId, SnapshotId=None,
                 Tags=None, Lifecycle=None, **kwargs):
        self.SnapshotId = SnapshotId or _next_id("fssnap")
        self.Name = Name
        self.VolumeId = VolumeId
        self.Tags = _convert_tags(Tags)
        self.Lifecycle = Lifecycle or "AVAILABLE"

    def to_dict(self):
        return {
            "SnapshotId": self.SnapshotId,
            "Name": self.Name,
            "VolumeId": self.VolumeId,
            "Tags": self.Tags,
            "Lifecycle": self.Lifecycle,
        }


class StorageVirtualMachineRecord:
    def __init__(self, FileSystemId, Name, StorageVirtualMachineId=None,
                 ActiveDirectoryConfiguration=None, SvmAdminPassword=None,
                 Tags=None, RootVolumeSecurityStyle=None, Lifecycle=None,
                 **kwargs):
        self.StorageVirtualMachineId = StorageVirtualMachineId or _next_id("svm")
        self.FileSystemId = FileSystemId
        self.Name = Name
        self.ActiveDirectoryConfiguration = ActiveDirectoryConfiguration
        self.SvmAdminPassword = SvmAdminPassword
        self.Tags = _convert_tags(Tags)
        self.RootVolumeSecurityStyle = RootVolumeSecurityStyle
        self.Lifecycle = Lifecycle or "CREATED"

    def to_dict(self):
        return {
            "StorageVirtualMachineId": self.StorageVirtualMachineId,
            "FileSystemId": self.FileSystemId,
            "Name": self.Name,
            "ActiveDirectoryConfiguration": self.ActiveDirectoryConfiguration,
            "SvmAdminPassword": self.SvmAdminPassword,
            "Tags": self.Tags,
            "RootVolumeSecurityStyle": self.RootVolumeSecurityStyle,
            "Lifecycle": self.Lifecycle,
        }


class FileCacheRecord:
    def __init__(self, FileCacheType, FileCacheTypeVersion, StorageCapacity,
                 SubnetIds, FileCacheId=None, SecurityGroupIds=None,
                 Tags=None, CopyTagsToDataRepositoryAssociations=None,
                 KmsKeyId=None, LustreConfiguration=None,
                 DataRepositoryAssociations=None, Lifecycle=None, **kwargs):
        self.FileCacheId = FileCacheId or _next_id("fc")
        self.FileCacheType = FileCacheType
        self.FileCacheTypeVersion = FileCacheTypeVersion
        self.StorageCapacity = StorageCapacity
        self.SubnetIds = SubnetIds or []
        self.SecurityGroupIds = SecurityGroupIds or []
        self.Tags = _convert_tags(Tags)
        self.CopyTagsToDataRepositoryAssociations = CopyTagsToDataRepositoryAssociations
        self.KmsKeyId = KmsKeyId
        self.LustreConfiguration = LustreConfiguration
        self.DataRepositoryAssociations = DataRepositoryAssociations or []
        self.Lifecycle = Lifecycle or "AVAILABLE"

    def to_dict(self):
        return {
            "FileCacheId": self.FileCacheId,
            "FileCacheType": self.FileCacheType,
            "FileCacheTypeVersion": self.FileCacheTypeVersion,
            "StorageCapacity": self.StorageCapacity,
            "SubnetIds": self.SubnetIds,
            "SecurityGroupIds": self.SecurityGroupIds,
            "Tags": self.Tags,
            "CopyTagsToDataRepositoryAssociations": self.CopyTagsToDataRepositoryAssociations,
            "KmsKeyId": self.KmsKeyId,
            "LustreConfiguration": self.LustreConfiguration,
            "DataRepositoryAssociations": self.DataRepositoryAssociations,
            "Lifecycle": self.Lifecycle,
        }


# === FSx Store ===

class FSxStore:
    """In-memory store for Amazon FSx resources."""

    def __init__(self):
        self._file_systems = {}
        self._backups = {}
        self._volumes = {}
        self._snapshots = {}
        self._svms = {}
        self._file_caches = {}

    # -- FileSystems --

    def file_systems(self, file_system_id=None):
        if file_system_id is not None:
            return self._file_systems.get(file_system_id)
        return list(self._file_systems.values())

    def create_file_system(self, FileSystemType, SubnetIds, **kwargs):
        record = FileSystemRecord(FileSystemType=FileSystemType, SubnetIds=SubnetIds, **kwargs)
        self._file_systems[record.FileSystemId] = record
        return record

    def get_file_system(self, file_system_id):
        r = self._file_systems.get(file_system_id)
        if not r:
            raise FileSystemNotFound(f"FileSystem '{file_system_id}' not found")
        return r

    def update_file_system(self, FileSystemId, **kwargs):
        r = self.get_file_system(FileSystemId)
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r

    def delete_file_system(self, file_system_id):
        self.get_file_system(file_system_id)
        del self._file_systems[file_system_id]

    # -- Backups --

    def backups(self, backup_id=None):
        if backup_id is not None:
            return self._backups.get(backup_id)
        return list(self._backups.values())

    def create_backup(self, FileSystemId=None, VolumeId=None, **kwargs):
        record = BackupRecord(FileSystemId=FileSystemId, VolumeId=VolumeId, **kwargs)
        self._backups[record.BackupId] = record
        return record

    def get_backup(self, backup_id):
        r = self._backups.get(backup_id)
        if not r:
            raise BackupNotFound(f"Backup '{backup_id}' not found")
        return r

    def copy_backup(self, SourceBackupId, **kwargs):
        _ = self.get_backup(SourceBackupId)
        record = BackupRecord(**kwargs)
        self._backups[record.BackupId] = record
        return record

    def delete_backup(self, backup_id):
        self.get_backup(backup_id)
        del self._backups[backup_id]

    # -- Volumes --

    def volumes(self, volume_id=None):
        if volume_id is not None:
            return self._volumes.get(volume_id)
        return list(self._volumes.values())

    def create_volume(self, VolumeType, Name, **kwargs):
        record = VolumeRecord(VolumeType=VolumeType, Name=Name, **kwargs)
        self._volumes[record.VolumeId] = record
        return record

    def get_volume(self, volume_id):
        r = self._volumes.get(volume_id)
        if not r:
            raise VolumeNotFound(f"Volume '{volume_id}' not found")
        return r

    def update_volume(self, VolumeId, **kwargs):
        r = self.get_volume(VolumeId)
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r

    def delete_volume(self, volume_id):
        self.get_volume(volume_id)
        del self._volumes[volume_id]

    # -- Snapshots --

    def snapshots(self, snapshot_id=None):
        if snapshot_id is not None:
            return self._snapshots.get(snapshot_id)
        return list(self._snapshots.values())

    def create_snapshot(self, Name, VolumeId, **kwargs):
        record = SnapshotRecord(Name=Name, VolumeId=VolumeId, **kwargs)
        self._snapshots[record.SnapshotId] = record
        return record

    def get_snapshot(self, snapshot_id):
        r = self._snapshots.get(snapshot_id)
        if not r:
            raise SnapshotNotFound(f"Snapshot '{snapshot_id}' not found")
        return r

    def update_snapshot(self, SnapshotId, Name, **kwargs):
        r = self.get_snapshot(SnapshotId)
        r.Name = Name
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r

    def delete_snapshot(self, snapshot_id):
        self.get_snapshot(snapshot_id)
        del self._snapshots[snapshot_id]

    # -- StorageVirtualMachines --

    def storage_virtual_machines(self, svm_id=None):
        if svm_id is not None:
            return self._svms.get(svm_id)
        return list(self._svms.values())

    def create_storage_virtual_machine(self, FileSystemId, Name, **kwargs):
        record = StorageVirtualMachineRecord(FileSystemId=FileSystemId, Name=Name, **kwargs)
        self._svms[record.StorageVirtualMachineId] = record
        return record

    def get_storage_virtual_machine(self, svm_id):
        r = self._svms.get(svm_id)
        if not r:
            raise StorageVirtualMachineNotFound(f"SVM '{svm_id}' not found")
        return r

    def update_storage_virtual_machine(self, StorageVirtualMachineId, **kwargs):
        r = self.get_storage_virtual_machine(StorageVirtualMachineId)
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r

    def delete_storage_virtual_machine(self, svm_id):
        self.get_storage_virtual_machine(svm_id)
        del self._svms[svm_id]

    # -- FileCaches --

    def file_caches(self, file_cache_id=None):
        if file_cache_id is not None:
            return self._file_caches.get(file_cache_id)
        return list(self._file_caches.values())

    def create_file_cache(self, FileCacheType, FileCacheTypeVersion,
                          StorageCapacity, SubnetIds, **kwargs):
        record = FileCacheRecord(
            FileCacheType=FileCacheType,
            FileCacheTypeVersion=FileCacheTypeVersion,
            StorageCapacity=StorageCapacity,
            SubnetIds=SubnetIds,
            **kwargs)
        self._file_caches[record.FileCacheId] = record
        return record

    def get_file_cache(self, file_cache_id):
        r = self._file_caches.get(file_cache_id)
        if not r:
            raise FileCacheNotFound(f"FileCache '{file_cache_id}' not found")
        return r

    def update_file_cache(self, FileCacheId, **kwargs):
        r = self.get_file_cache(FileCacheId)
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r

    def delete_file_cache(self, file_cache_id):
        self.get_file_cache(file_cache_id)
        del self._file_caches[file_cache_id]
