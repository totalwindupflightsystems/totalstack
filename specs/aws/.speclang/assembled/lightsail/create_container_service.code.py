# spec:trace: aws/lightsail/create_container_service.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-container-service
# spec:generated: DO NOT EDIT — edit the spec instead

def create_container_service(store, request: dict) -> dict:
    """Creates an Amazon Lightsail container service. A Lightsail container service is a compute resource to which you can deploy containers. For more information, see Container services in Amazon Lightsail """
    power = request.get("power", "").strip() if isinstance(request.get("power"), str) else request.get("power")
    if not power:
        raise ValidationException("power is required")
    scale = request.get("scale", "").strip() if isinstance(request.get("scale"), str) else request.get("scale")
    if not scale:
        raise ValidationException("scale is required")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    if store.container_services(service_name):
        raise ResourceInUseException("Resource service_name already exists")

    record = {
        "serviceName": service_name,
        "power": power,
        "scale": scale,
        "tags": tags,
        "publicDomainNames": public_domain_names,
        "deployment": deployment,
        "privateRegistryAccess": private_registry_access,
    }

    store.container_services(service_name, record)

    return {
        "containerService": record.get("containerService", {}),
    }

