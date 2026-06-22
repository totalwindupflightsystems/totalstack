def handler(store, request: dict) -> dict:
    sn = request.get("SnapshotName")
    return store.describe_snapshots(SnapshotName=sn)

