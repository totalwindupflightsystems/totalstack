def handler(store, request: dict) -> dict:
    """DeleteDBSnapshot handler."""
    return store.delete_db_snapshot(
        db_snapshot_identifier=request["DBSnapshotIdentifier"])
