# spec:trace: aws/lightsail/disable_add_on.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/disable-add-on
# spec:generated: DO NOT EDIT — edit the spec instead

def disable_add_on(store, request: dict) -> dict:
    """Disables an add-on for an Amazon Lightsail resource. For more information, see the Amazon Lightsail Developer Guide ."""
    add_on_type = request.get("addOnType", "").strip() if isinstance(request.get("addOnType"), str) else request.get("addOnType")
    if not add_on_type:
        raise ValidationException("addOnType is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    if store.disable_add_ons(resource_name):
        raise ResourceInUseException("Resource resource_name already exists")

    record = {
        "addOnType": add_on_type,
        "resourceName": resource_name,
    }

    store.disable_add_ons(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }

