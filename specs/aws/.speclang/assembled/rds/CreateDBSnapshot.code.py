def handler(store, request: dict) -> dict:
    """CreateDBSnapshot handler."""
    return store.create_db_snapshot(
        db_snapshot_identifier=request["DBSnapshotIdentifier"],
        db_instance_identifier=request["DBInstanceIdentifier"],
        tags=request.get("Tags"))
