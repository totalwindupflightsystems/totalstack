# spec:trace: aws/lightsail/create_instance_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-instance-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def create_instance_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of a specific virtual private server, or instance . You can use a snapshot to create a new instance that is based on that snapshot. The create instance snapshot operation supports t"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    instance_snapshot_name = request.get("instanceSnapshotName", "").strip() if isinstance(request.get("instanceSnapshotName"), str) else request.get("instanceSnapshotName")
    if not instance_snapshot_name:
        raise ValidationException("instanceSnapshotName is required")

    if store.instance_snapshots(instance_snapshot_name):
        raise ResourceInUseException("Resource instance_snapshot_name already exists")

    record = {
        "instanceSnapshotName": instance_snapshot_name,
        "instanceName": instance_name,
        "tags": tags,
    }

    store.instance_snapshots(instance_snapshot_name, record)

    return {
        "operations": record.get("operations", {}),
    }

