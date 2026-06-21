def handler(store, request: dict) -> dict:
    """DeleteDBInstance handler."""
    return store.delete_db_instance(
        db_instance_identifier=request["DBInstanceIdentifier"],
        skip_final_snapshot=request.get("SkipFinalSnapshot", False),
        final_db_snapshot_identifier=request.get("FinalDBSnapshotIdentifier"))
