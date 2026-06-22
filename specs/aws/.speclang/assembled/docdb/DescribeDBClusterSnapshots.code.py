def handler(store, request: dict):
    return store.describe_snapshots(request.get("DBClusterSnapshotIdentifier"), request.get("DBClusterIdentifier"))
