# spec:trace: aws/lightsail/get_relational_database_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-relational-database-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def get_relational_database_snapshot(store, request: dict) -> dict:
    """Returns information about a specific database snapshot in Amazon Lightsail."""
    relational_database_snapshot_name = request.get("relationalDatabaseSnapshotName", "").strip() if isinstance(request.get("relationalDatabaseSnapshotName"), str) else request.get("relationalDatabaseSnapshotName")
    if not relational_database_snapshot_name:
        raise ValidationException("relationalDatabaseSnapshotName is required")

    resource = store.relational_database_snapshots(relational_database_snapshot_name)
    if not resource:
        raise ResourceNotFoundException("Resource relational_database_snapshot_name not found")
    return {"relationalDatabaseSnapshotName": relational_database_snapshot_name, **resource}

