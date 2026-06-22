def handler(store, request: dict):
    cluster_id = request["DBClusterIdentifier"]
    snapshot_id = request["DBClusterSnapshotIdentifier"]
    engine = request["Engine"]
    return store.restore_cluster_from_snapshot(cluster_id, snapshot_id, engine, **{k: v for k, v in request.items() if k not in ("DBClusterIdentifier", "DBClusterSnapshotIdentifier", "Engine")})
