# spec:trace: aws/lightsail/create_relational_database_from_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-relational-database-from-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def create_relational_database_from_snapshot(store, request: dict) -> dict:
    """Creates a new database from an existing database snapshot in Amazon Lightsail. You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to """
    relational_database_name = request.get("relationalDatabaseName", "").strip() if isinstance(request.get("relationalDatabaseName"), str) else request.get("relationalDatabaseName")
    if not relational_database_name:
        raise ValidationException("relationalDatabaseName is required")

    if store.relational_database_from_snapshots(relational_database_name):
        raise ResourceInUseException("Resource relational_database_name already exists")

    record = {
        "relationalDatabaseName": relational_database_name,
        "availabilityZone": availability_zone,
        "publiclyAccessible": publicly_accessible,
        "relationalDatabaseSnapshotName": relational_database_snapshot_name,
        "relationalDatabaseBundleId": relational_database_bundle_id,
        "sourceRelationalDatabaseName": source_relational_database_name,
        "restoreTime": restore_time,
        "useLatestRestorableTime": use_latest_restorable_time,
        "tags": tags,
    }

    store.relational_database_from_snapshots(relational_database_name, record)

    return {
        "operations": record.get("operations", {}),
    }

