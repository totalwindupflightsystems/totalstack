# spec:trace: aws/lightsail/create_relational_database_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-relational-database-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def create_relational_database_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database. The create relational database sn"""
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")
    relational_database_snapshot_name = request.get("relationalDatabaseSnapshotName", "").strip() if isinstance(request.get("relationalDatabaseSnapshotName"), str) else request.get("relationalDatabaseSnapshotName")
    if not relational_database_snapshot_name:
        raise ValidationException("relationalDatabaseSnapshotName is required")

    if store.relational_database_snapshots(relational_database_name):
        raise ResourceInUseException("Resource relational_database_name already exists")

    record = {
        "relationalDatabaseName": relational_database_name,
        "relationalDatabaseSnapshotName": relational_database_snapshot_name,
        "tags": tags,
    }

    store.relational_database_snapshots(relational_database_name, record)

    return {
        "operations": record.get("operations", {}),
    }

