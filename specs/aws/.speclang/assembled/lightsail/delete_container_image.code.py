# spec:trace: aws/lightsail/delete_container_image.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/delete-container-image
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_container_image(store, request: dict) -> dict:
    """Deletes a container image that is registered to your Amazon Lightsail container service."""
    request.get("image", "").strip() if isinstance(request.get("image"), str) else request.get("image")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")

    if not store.container_images(service_name):
        raise ResourceNotFoundException("Resource service_name not found")
    store.delete_container_images(service_name)
    return {}

