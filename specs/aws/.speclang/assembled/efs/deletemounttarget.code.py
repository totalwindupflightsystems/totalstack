def handler(store, r: dict) -> dict:
    return store.delete_mount_target(r['MountTargetId'])