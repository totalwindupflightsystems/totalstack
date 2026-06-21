# spec:trace: aws/lightsail/close_instance_public_ports.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/close-instance-public-ports
# spec:generated: DO NOT EDIT — edit the spec instead

def close_instance_public_ports(store, request: dict) -> dict:
    """Closes ports for a specific Amazon Lightsail instance. The CloseInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For """
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    port_info = request.get("portInfo", "").strip() if isinstance(request.get("portInfo"), str) else request.get("portInfo")
    if not port_info:
        raise ValidationException("portInfo is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CloseInstancePublicPorts", request)

