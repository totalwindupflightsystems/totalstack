# spec:trace: aws/lightsail/delete_instance_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-instance-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_instance_snapshot(store, request: dict) -> dict:
    """Deletes a specific snapshot of a virtual private server (or instance ). The delete instance snapshot operation supports tag-based access control via resource tags applied to the resource identified by"""
    instance_snapshot_name = request.get("instanceSnapshotName", "").strip() if isinstance(request.get("instanceSnapshotName"), str) else request.get("instanceSnapshotName")

    if not store.instance_snapshots(instance_snapshot_name):
        raise ResourceNotFoundException("Resource instance_snapshot_name not found")
    store.delete_instance_snapshots(instance_snapshot_name)
    return {}

