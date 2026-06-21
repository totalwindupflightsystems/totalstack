# spec:trace: aws/lightsail/open_instance_public_ports.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/open-instance-public-ports
# spec:generated: DO NOT EDIT — edit the spec instead

def open_instance_public_ports(store, request: dict) -> dict:
    """Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol. The OpenInstancePublicPorts action supports"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    port_info = request.get("portInfo", "").strip() if isinstance(request.get("portInfo"), str) else request.get("portInfo")
    if not port_info:
        raise ValidationException("portInfo is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("OpenInstancePublicPorts", request)

