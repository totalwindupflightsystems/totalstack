# spec:trace: aws/lightsail/create_disk_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-disk-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def create_disk_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance. You can take a snapshot of an attach"""
    disk_snapshot_name = request.get("diskSnapshotName", "").strip() if isinstance(request.get("diskSnapshotName"), str) else request.get("diskSnapshotName")
    if not disk_snapshot_name:
        raise ValidationException("diskSnapshotName is required")

    if store.disk_snapshots(disk_snapshot_name):
        raise ResourceInUseException("Resource disk_snapshot_name already exists")

    record = {
        "diskName": disk_name,
        "diskSnapshotName": disk_snapshot_name,
        "instanceName": instance_name,
        "tags": tags,
    }

    store.disk_snapshots(disk_snapshot_name, record)

    return {
        "operations": record.get("operations", {}),
    }

