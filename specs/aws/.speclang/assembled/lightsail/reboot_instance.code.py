# spec:trace: aws/lightsail/reboot_instance.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/reboot-instance
# spec:generated: DO NOT EDIT — edit the spec instead

def reboot_instance(store, request: dict) -> dict:
    """Restarts a specific instance. The reboot instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Amaz"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RebootInstance", request)

