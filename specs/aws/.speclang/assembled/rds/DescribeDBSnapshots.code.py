def handler(store, request: dict) -> dict:
    """DescribeDBSnapshots handler."""
    result = store.describe_db_snapshots(
        db_snapshot_identifier=request.get("DBSnapshotIdentifier"),
        db_instance_identifier=request.get("DBInstanceIdentifier"),
        snapshot_type=request.get("SnapshotType"))
    return {"DBSnapshots": result}
