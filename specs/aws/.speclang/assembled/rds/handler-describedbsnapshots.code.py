def handler(store, request: dict) -> dict:
    identifier = request.get("DBSnapshotIdentifier")
    return store.describe_snapshots(identifier)
