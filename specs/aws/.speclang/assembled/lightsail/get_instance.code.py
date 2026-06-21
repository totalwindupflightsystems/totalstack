# spec:trace: aws/lightsail/get_instance.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instance
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instance(store, request: dict) -> dict:
    """Returns information about a specific Amazon Lightsail instance, which is a virtual private server."""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instances(instance_name)
    if not resource:
        raise ResourceNotFoundException("Resource instance_name not found")
    return {"instanceName": instance_name, **resource}

