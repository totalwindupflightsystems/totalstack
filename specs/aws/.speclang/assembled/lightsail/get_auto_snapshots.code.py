# spec:trace: aws/lightsail/get_auto_snapshots.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-auto-snapshots
# spec:generated: DO NOT EDIT — edit the spec instead

def get_auto_snapshots(store, request: dict) -> dict:
    """Returns the available automatic snapshots for an instance or disk. For more information, see the Amazon Lightsail Developer Guide ."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.auto_snapshotss(resource_name)
    if not resource:
        raise ResourceNotFoundException("Resource resource_name not found")
    return {"resourceName": resource_name, **resource}

