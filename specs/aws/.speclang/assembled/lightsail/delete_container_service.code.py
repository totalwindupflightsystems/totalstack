# spec:trace: aws/lightsail/delete_container_service.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-container-service
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_container_service(store, request: dict) -> dict:
    """Deletes your Amazon Lightsail container service."""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")

    if not store.container_services(service_name):
        raise ResourceNotFoundException("Resource service_name not found")
    store.delete_container_services(service_name)
    return {}

