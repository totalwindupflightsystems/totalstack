# spec:trace: aws/lightsail/get_disk_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-disk-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def get_disk_snapshot(store, request: dict) -> dict:
    """Returns information about a specific block storage disk snapshot."""
    disk_snapshot_name = request.get("diskSnapshotName", "").strip() if isinstance(request.get("diskSnapshotName"), str) else request.get("diskSnapshotName")
    if not disk_snapshot_name:
        raise ValidationException("diskSnapshotName is required")

    resource = store.disk_snapshots(disk_snapshot_name)
    if not resource:
        raise ResourceNotFoundException("Resource disk_snapshot_name not found")
    return {"diskSnapshotName": disk_snapshot_name, **resource}

