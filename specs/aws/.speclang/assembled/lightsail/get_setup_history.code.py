# spec:trace: aws/lightsail/get_setup_history.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-setup-history
# spec:generated: DO NOT EDIT — edit the spec instead

def get_setup_history(store, request: dict) -> dict:
    """Returns detailed information for five of the most recent SetupInstanceHttps requests that were ran on the target instance."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.setup_historys(resource_name)
    if not resource:
        raise ResourceNotFoundException("Resource resource_name not found")
    return {"resourceName": resource_name, **resource}

