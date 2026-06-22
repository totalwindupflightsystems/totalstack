"""EFS Store — Elastic File System emulation."""
class ResourceNotFoundException(Exception): pass
class FileSystemAlreadyExists(Exception): pass
class InvalidParameterException(Exception): pass

class EfsStore:
    def __init__(self):
        self._filesystems: dict[str, dict] = {}
        self._mount_targets: dict[str, dict] = {}
        self._tags: dict[str, list] = {}
    
    def create_filesystem(self, token: str, **kwargs) -> dict:
        fs_id = f'fs-{len(self._filesystems) + 1:08d}'
        fs = {
            'FileSystemId': fs_id,
            'CreationToken': token,
            'LifeCycleState': 'available',
            'PerformanceMode': kwargs.get('PerformanceMode', 'generalPurpose'),
            'CreationTime': 1625000000.0,
            **kwargs
        }
        self._filesystems[fs_id] = fs
        return fs
    
    def describe_filesystems(self, fs_id: str = None, token: str = None) -> dict:
        if fs_id:
            if fs_id not in self._filesystems:
                raise ResourceNotFoundException(f"FileSystem {fs_id} not found")
            return {'FileSystems': [self._filesystems[fs_id]]}
        fss = list(self._filesystems.values())
        if token:
            fss = [f for f in fss if f['CreationToken'] == token]
        return {'FileSystems': fss}
    
    def delete_filesystem(self, fs_id: str) -> dict:
        if fs_id not in self._filesystems:
            raise ResourceNotFoundException(f"FileSystem {fs_id} not found")
        del self._filesystems[fs_id]
        return {}
    
    def create_mount_target(self, fs_id: str, subnet_id: str, **kwargs) -> dict:
        if fs_id not in self._filesystems:
            raise ResourceNotFoundException(f"FileSystem {fs_id} not found")
        mt_id = f'fsmt-{len(self._mount_targets) + 1:08d}'
        mt = {
            'MountTargetId': mt_id,
            'FileSystemId': fs_id,
            'SubnetId': subnet_id,
            'LifeCycleState': 'available',
            **kwargs
        }
        self._mount_targets[mt_id] = mt
        return mt
    
    def describe_mount_targets(self, fs_id: str = None, mt_id: str = None) -> dict:
        if mt_id:
            if mt_id not in self._mount_targets:
                raise ResourceNotFoundException(f"MountTarget {mt_id} not found")
            return {'MountTargets': [self._mount_targets[mt_id]]}
        mts = list(self._mount_targets.values())
        if fs_id:
            mts = [m for m in mts if m['FileSystemId'] == fs_id]
        return {'MountTargets': mts}
    
    def delete_mount_target(self, mt_id: str) -> dict:
        if mt_id not in self._mount_targets:
            raise ResourceNotFoundException(f"MountTarget {mt_id} not found")
        del self._mount_targets[mt_id]
        return {}
    
    def tag_resource(self, resource_id: str, tags: list) -> dict:
        self._tags.setdefault(resource_id, []).extend(tags)
        return {}
    
    def list_tags(self, resource_id: str) -> dict:
        return {'Tags': self._tags.get(resource_id, [])}
    
    def untag_resource(self, resource_id: str, tag_keys: list) -> dict:
        if resource_id in self._tags:
            self._tags[resource_id] = [t for t in self._tags[resource_id] if t['Key'] not in tag_keys]
        return {}
