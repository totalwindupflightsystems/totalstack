def handler(store, request: dict):
    return store.copy_snapshot(request["SourceDBClusterSnapshotIdentifier"], request["TargetDBClusterSnapshotIdentifier"])
