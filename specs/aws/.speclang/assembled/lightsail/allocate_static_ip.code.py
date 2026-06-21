# spec:trace: aws/lightsail/allocate_static_ip.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/allocate-static-ip
# spec:generated: DO NOT EDIT — edit the spec instead

def allocate_static_ip(store, request: dict) -> dict:
    """Allocates a static IP address."""
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AllocateStaticIp", request)

