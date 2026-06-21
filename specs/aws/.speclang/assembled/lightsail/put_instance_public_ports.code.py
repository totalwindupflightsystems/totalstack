# spec:trace: aws/lightsail/put_instance_public_ports.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/put-instance-public-ports
# spec:generated: DO NOT EDIT — edit the spec instead

def put_instance_public_ports(store, request: dict) -> dict:
    """Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol. This action also closes all currently open """
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    port_infos = request.get("portInfos", "").strip() if isinstance(request.get("portInfos"), str) else request.get("portInfos")
    if not port_infos:
        raise ValidationException("portInfos is required")

    if store.instance_public_portss(instance_name):
        raise ResourceInUseException("Resource instance_name already exists")

    record = {
        "portInfos": port_infos,
        "instanceName": instance_name,
    }

    store.instance_public_portss(instance_name, record)

    return {
        "operation": record.get("operation", {}),
    }

