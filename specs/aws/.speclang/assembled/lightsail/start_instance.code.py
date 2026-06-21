# spec:trace: aws/lightsail/start_instance.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/start-instance
# spec:generated: DO NOT EDIT — edit the spec instead

def start_instance(store, request: dict) -> dict:
    """Starts a specific Amazon Lightsail instance from a stopped state. To restart an instance, use the reboot instance operation. When you start a stopped instance, Lightsail assigns a new public IP addres"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    if store.instances(instance_name):
        raise ResourceInUseException("Resource instance_name already exists")

    record = {
        "instanceName": instance_name,
    }

    store.instances(instance_name, record)

    return {
        "operations": record.get("operations", {}),
    }

