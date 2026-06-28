def handler(store, request: dict) -> dict:
    store.delete_snapshot(request["SnapshotId"])
    return {}
