# spec:trace: aws/lightsail/enable_add_on.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/enable-add-on
# spec:generated: DO NOT EDIT — edit the spec instead

def enable_add_on(store, request: dict) -> dict:
    """Enables or modifies an add-on for an Amazon Lightsail resource. For more information, see the Amazon Lightsail Developer Guide ."""
    add_on_request = request.get("addOnRequest", "").strip() if isinstance(request.get("addOnRequest"), str) else request.get("addOnRequest")
    if not add_on_request:
        raise ValidationException("addOnRequest is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.enable_add_ons(resource_name):
        raise ResourceInUseException("Resource resource_name already exists")

    record = {
        "resourceName": resource_name,
        "addOnRequest": add_on_request,
    }

    store.enable_add_ons(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }

