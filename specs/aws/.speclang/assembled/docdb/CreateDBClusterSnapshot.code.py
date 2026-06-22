def handler(store, request: dict):
    return store.create_snapshot(request["DBClusterSnapshotIdentifier"], request["DBClusterIdentifier"])
