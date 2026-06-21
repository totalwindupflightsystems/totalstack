# spec:trace: aws/lightsail/get_instance_port_states.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-instance-port-states
# spec:generated: DO NOT EDIT — edit the spec instead

def get_instance_port_states(store, request: dict) -> dict:
    """Returns the firewall port states for a specific Amazon Lightsail instance, the IP addresses allowed to connect to the instance through the ports, and the protocol."""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_port_statess(instance_name)
    if not resource:
        raise ResourceNotFoundException("Resource instance_name not found")
    return {"instanceName": instance_name, **resource}

