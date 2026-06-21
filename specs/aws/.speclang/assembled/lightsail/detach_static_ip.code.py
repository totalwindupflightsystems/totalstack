# spec:trace: aws/lightsail/detach_static_ip.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/detach-static-ip
# spec:generated: DO NOT EDIT — edit the spec instead

def detach_static_ip(store, request: dict) -> dict:
    """Detaches a static IP from the Amazon Lightsail instance to which it is attached."""
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachStaticIp", request)

