# spec:trace: aws/lightsail/set_ip_address_type.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/set-ip-address-type
# spec:generated: DO NOT EDIT — edit the spec instead

def set_ip_address_type(store, request: dict) -> dict:
    """Sets the IP address type for an Amazon Lightsail resource. Use this action to enable dual-stack for a resource, which enables IPv4 and IPv6 for the specified resource. Alternately, you can use this ac"""
    ip_address_type = request.get("ipAddressType", "").strip() if isinstance(request.get("ipAddressType"), str) else request.get("ipAddressType")
    if not ip_address_type:
        raise ValidationException("ipAddressType is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")
    resource_type = request.get("resourceType", "").strip() if isinstance(request.get("resourceType"), str) else request.get("resourceType")
    if not resource_type:
        raise ValidationException("resourceType is required")

    if store.set_ip_address_types(resource_name):
        raise ResourceInUseException("Resource resource_name already exists")

    record = {
        "resourceType": resource_type,
        "resourceName": resource_name,
        "ipAddressType": ip_address_type,
        "acceptBundleUpdate": accept_bundle_update,
    }

    store.set_ip_address_types(resource_name, record)

    return {
        "operations": record.get("operations", {}),
    }

