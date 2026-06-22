def handler(store, request: dict) -> dict:
    record = store.delete_cluster_snapshot(request["SnapshotIdentifier"])
    return {"Snapshot": record.to_dict()}
