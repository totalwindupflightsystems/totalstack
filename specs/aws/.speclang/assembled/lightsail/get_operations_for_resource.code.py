# spec:trace: aws/lightsail/get_operations_for_resource.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-operations-for-resource
# spec:generated: DO NOT EDIT — edit the spec instead

def get_operations_for_resource(store, request: dict) -> dict:
    """Gets operations for a specific resource (an instance or a static IP)."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.operations_for_resources(resource_name)
    if not resource:
        raise ResourceNotFoundException("Resource resource_name not found")
    return {"resourceName": resource_name, **resource}

