def handler(store, r: dict) -> dict:
    return store.describe_mount_targets(r.get('FileSystemId'), r.get('MountTargetId'))