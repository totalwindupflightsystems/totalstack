# spec:trace: aws/lightsail/delete_relational_database_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-relational-database-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_relational_database_snapshot(store, request: dict) -> dict:
    """Deletes a database snapshot in Amazon Lightsail. The delete relational database snapshot operation supports tag-based access control via resource tags applied to the resource identified by relationalD"""
    relational_database_snapshot_name = request.get("relationalDatabaseSnapshotName", "").strip() if isinstance(request.get("relationalDatabaseSnapshotName"), str) else request.get("relationalDatabaseSnapshotName")

    if not store.relational_database_snapshots(relational_database_snapshot_name):
        raise ResourceNotFoundException("Resource relational_database_snapshot_name not found")
    store.delete_relational_database_snapshots(relational_database_snapshot_name)
    return {}

