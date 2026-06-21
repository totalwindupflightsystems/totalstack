# spec:trace: aws/lightsail/get_instance_state.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instance-state
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instance_state(store, request: dict) -> dict:
    """Returns the state of a specific instance. Works on one instance at a time."""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_states(instance_name)
    if not resource:
        raise ResourceNotFoundException("Resource instance_name not found")
    return {"instanceName": instance_name, **resource}

