def _find_by_arn(store, arn: str):
    """Find a resource record by its ARN."""
    for coll in [store.file_systems(), store.backups(), store.volumes(),
                 store.snapshots(), store.storage_virtual_machines(),
                 store.file_caches()]:
        for r in coll:
            rid = (getattr(r, 'FileSystemId', None) or
                   getattr(r, 'BackupId', None) or
                   getattr(r, 'VolumeId', None) or
                   getattr(r, 'SnapshotId', None) or
                   getattr(r, 'StorageVirtualMachineId', None) or
                   getattr(r, 'FileCacheId', None))
            if rid and rid in arn:
                return r
    raise ResourceNotFound(f"Resource '{arn}' not found")
