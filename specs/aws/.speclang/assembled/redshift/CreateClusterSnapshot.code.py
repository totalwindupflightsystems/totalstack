def handler(store, request: dict) -> dict:
    record = store.create_cluster_snapshot(
        request["SnapshotIdentifier"],
        request["ClusterIdentifier"],
        ManualSnapshotRetentionPeriod=request.get("ManualSnapshotRetentionPeriod"),
        Tags=request.get("Tags"))
    return {"Snapshot": record.to_dict()}
