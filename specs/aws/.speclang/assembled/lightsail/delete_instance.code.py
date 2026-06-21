# spec:trace: aws/lightsail/delete_instance.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-instance
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_instance(store, request: dict) -> dict:
    """Deletes an Amazon Lightsail instance. The delete instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see """
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")

    if not store.instances(instance_name):
        raise ResourceNotFoundException("Resource instance_name not found")
    store.delete_instances(instance_name)
    return {}

