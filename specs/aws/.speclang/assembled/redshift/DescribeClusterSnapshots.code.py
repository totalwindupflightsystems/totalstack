def handler(store, request: dict) -> dict:
    return store.describe_cluster_snapshots(
        SnapshotIdentifier=request.get("SnapshotIdentifier"),
        ClusterIdentifier=request.get("ClusterIdentifier"))
