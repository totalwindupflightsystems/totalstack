# spec:trace: aws/lightsail/stop_instance.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/stop-instance
# spec:generated: DO NOT EDIT — edit the spec instead

def stop_instance(store, request: dict) -> dict:
    """Stops a specific Amazon Lightsail instance that is currently running. When you start a stopped instance, Lightsail assigns a new public IP address to the instance. To use the same IP address after sto"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")

    if not store.instances(instance_name):
        raise ResourceNotFoundException("Resource instance_name not found")
    store.delete_instances(instance_name)
    return {}

