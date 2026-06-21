# spec:trace: aws/lightsail/get_instance_access_details.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instance-access-details
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instance_access_details(store, request: dict) -> dict:
    """Returns temporary SSH keys you can use to connect to a specific virtual private server, or instance . The get instance access details operation supports tag-based access control via resource tags appl"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_access_detailss(instance_name)
    if not resource:
        raise ResourceNotFoundException("Resource instance_name not found")
    return {"instanceName": instance_name, **resource}

