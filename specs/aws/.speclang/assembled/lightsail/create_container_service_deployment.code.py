# spec:trace: aws/lightsail/create_container_service_deployment.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/create-container-service-deployment
# spec:generated: DO NOT EDIT — edit the spec instead

def create_container_service_deployment(store, request: dict) -> dict:
    """Creates a deployment for your Amazon Lightsail container service. A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, th"""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    if store.container_service_deployments(service_name):
        raise ResourceInUseException("Resource service_name already exists")

    record = {
        "serviceName": service_name,
        "containers": containers,
        "publicEndpoint": public_endpoint,
    }

    store.container_service_deployments(service_name, record)

    return {
        "containerService": record.get("containerService", {}),
    }

