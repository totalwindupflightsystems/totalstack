# spec:trace: aws/lightsail/delete_auto_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-auto-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_auto_snapshot(store, request: dict) -> dict:
    """Deletes an automatic snapshot of an instance or disk. For more information, see the Amazon Lightsail Developer Guide ."""
    request.get("date", "").strip() if isinstance(request.get("date"), str) else request.get("date")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")

    if not store.auto_snapshots(resource_name):
        raise ResourceNotFoundException("Resource resource_name not found")
    store.delete_auto_snapshots(resource_name)
    return {}

