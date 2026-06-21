# spec:trace: aws/lightsail/get_container_service_deployments.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-service-deployments
# spec:generated: DO NOT EDIT — edit the spec instead

def get_container_service_deployments(store, request: dict) -> dict:
    """Returns the deployments for your Amazon Lightsail container service A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service"""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_service_deploymentss(service_name)
    if not resource:
        raise ResourceNotFoundException("Resource service_name not found")
    return {"serviceName": service_name, **resource}

