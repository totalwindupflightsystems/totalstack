# spec:trace: aws/lightsail/delete_known_host_keys.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-known-host-keys
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_known_host_keys(store, request: dict) -> dict:
    """Deletes the known host key or certificate used by the Amazon Lightsail browser-based SSH or RDP clients to authenticate an instance. This operation enables the Lightsail browser-based SSH or RDP clien"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")

    if not store.known_host_keyss(instance_name):
        raise ResourceNotFoundException("Resource instance_name not found")
    store.delete_known_host_keyss(instance_name)
    return {}

