# spec:trace: aws/lightsail/delete_disk_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-disk-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_disk_snapshot(store, request: dict) -> dict:
    """Deletes the specified disk snapshot. When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved i"""
    disk_snapshot_name = request.get("diskSnapshotName", "").strip() if isinstance(request.get("diskSnapshotName"), str) else request.get("diskSnapshotName")

    if not store.disk_snapshots(disk_snapshot_name):
        raise ResourceNotFoundException("Resource disk_snapshot_name not found")
    store.delete_disk_snapshots(disk_snapshot_name)
    return {}

