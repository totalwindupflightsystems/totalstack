# spec:trace: aws/lightsail/get_static_ip.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-static-ip
# spec:generated: DO NOT EDIT — edit the spec instead

def get_static_ip(store, request: dict) -> dict:
    """Returns information about an Amazon Lightsail static IP."""
    static_ip_name = request.get("staticIpName", "").strip() if isinstance(request.get("staticIpName"), str) else request.get("staticIpName")
    if not static_ip_name:
        raise ValidationException("staticIpName is required")

    resource = store.static_ips(static_ip_name)
    if not resource:
        raise ResourceNotFoundException("Resource static_ip_name not found")
    return {"staticIpName": static_ip_name, **resource}

