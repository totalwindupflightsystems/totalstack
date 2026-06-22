def handler(store, request: dict):
    return store.delete_snapshot(request["DBClusterSnapshotIdentifier"])
