# spec:trace: aws/lightsail/attach_static_ip.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/attach-static-ip
# spec:generated: DO NOT EDIT — edit the spec instead

def attach_static_ip(store, request: dict) -> dict:
    """Attaches a static IP address to a specific Amazon Lightsail instance."""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachStaticIp", request)

