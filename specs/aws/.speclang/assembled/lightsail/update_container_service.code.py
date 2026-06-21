# spec:trace: aws/lightsail/update_container_service.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/update-container-service
# spec:generated: DO NOT EDIT — edit the spec instead

def update_container_service(store, request: dict) -> dict:
    """Updates the configuration of your Amazon Lightsail container service, such as its power, scale, and public domain names."""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_services(service_name)
    if not resource:
        raise ResourceNotFoundException("Resource service_name not found")

    # Update mutable fields
    if "power" in request:
        resource["power"] = power
    if "scale" in request:
        resource["scale"] = scale
    if "isDisabled" in request:
        resource["isDisabled"] = is_disabled
    if "publicDomainNames" in request:
        resource["publicDomainNames"] = public_domain_names
    if "privateRegistryAccess" in request:
        resource["privateRegistryAccess"] = private_registry_access

    store.container_services(service_name, resource)
    return resource

