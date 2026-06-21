def handler(store, request: dict) -> dict:
    return store.create_snapshot(request["DBSnapshotIdentifier"], request["DBInstanceIdentifier"])
