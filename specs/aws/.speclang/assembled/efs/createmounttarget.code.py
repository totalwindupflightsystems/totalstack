def handler(store, r: dict) -> dict:
    return store.create_mount_target(r['FileSystemId'], r['SubnetId'])