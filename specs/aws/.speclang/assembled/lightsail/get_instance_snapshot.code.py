# spec:trace: aws/lightsail/get_instance_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instance-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instance_snapshot(store, request: dict) -> dict:
    """Returns information about a specific instance snapshot."""
    instance_snapshot_name = request.get("instanceSnapshotName", "").strip() if isinstance(request.get("instanceSnapshotName"), str) else request.get("instanceSnapshotName")
    if not instance_snapshot_name:
        raise ValidationException("instanceSnapshotName is required")

    resource = store.instance_snapshots(instance_snapshot_name)
    if not resource:
        raise ResourceNotFoundException("Resource instance_snapshot_name not found")
    return {"instanceSnapshotName": instance_snapshot_name, **resource}

