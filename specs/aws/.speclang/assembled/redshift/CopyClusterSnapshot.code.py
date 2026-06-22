def handler(store, request: dict) -> dict:
    record = store.copy_cluster_snapshot(
        request["SourceSnapshotIdentifier"],
        request["TargetSnapshotIdentifier"],
        ManualSnapshotRetentionPeriod=request.get("ManualSnapshotRetentionPeriod"))
    return {"Snapshot": record.to_dict()}
