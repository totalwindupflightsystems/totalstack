# spec:trace: aws/lightsail/release_static_ip.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/release-static-ip
# spec:generated: DO NOT EDIT — edit the spec instead

def release_static_ip(store, request: dict) -> dict:
    """Deletes a specific static IP from your account."""
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ReleaseStaticIp", request)

