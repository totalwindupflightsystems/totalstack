# spec:trace: aws/lightsail/get_container_images.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/get-container-images
# spec:generated: DO NOT EDIT — edit the spec instead

def get_container_images(store, request: dict) -> dict:
    """Returns the container images that are registered to your Amazon Lightsail container service. If you created a deployment on your Lightsail container service that uses container images from a public re"""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_imagess(service_name)
    if not resource:
        raise ResourceNotFoundException("Resource service_name not found")
    return {"serviceName": service_name, **resource}

