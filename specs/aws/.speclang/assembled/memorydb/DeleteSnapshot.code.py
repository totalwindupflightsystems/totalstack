def handler(store, request: dict) -> dict:
    return store.delete_snapshot(request["SnapshotName"])

