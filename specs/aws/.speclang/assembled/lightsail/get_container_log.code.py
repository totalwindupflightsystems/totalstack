# spec:trace: aws/lightsail/get_container_log.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-log
# spec:generated: DO NOT EDIT — edit the spec instead

def get_container_log(store, request: dict) -> dict:
    """Returns the log events of a container of your Amazon Lightsail container service. If your container service has more than one node (i.e., a scale greater than 1), then the log events that are returned"""
    container_name = request.get("containerName", "").strip() if isinstance(request.get("containerName"), str) else request.get("containerName")
    if not container_name:
        raise ValidationException("containerName is required")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_logs(service_name)
    if not resource:
        raise ResourceNotFoundException("Resource service_name not found")
    return {"serviceName": service_name, **resource}

