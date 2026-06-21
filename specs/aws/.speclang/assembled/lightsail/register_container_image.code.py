# spec:trace: aws/lightsail/register_container_image.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/register-container-image
# spec:generated: DO NOT EDIT — edit the spec instead

def register_container_image(store, request: dict) -> dict:
    """Registers a container image to your Amazon Lightsail container service. This action is not required if you install and use the Lightsail Control (lightsailctl) plugin to push container images to your """
    digest = request.get("digest", "").strip() if isinstance(request.get("digest"), str) else request.get("digest")
    if not digest:
        raise ValidationException("digest is required")
    label = request.get("label", "").strip() if isinstance(request.get("label"), str) else request.get("label")
    if not label:
        raise ValidationException("label is required")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    if store.register_container_images(service_name):
        raise ResourceInUseException("Resource service_name already exists")

    record = {
        "serviceName": service_name,
        "label": label,
        "digest": digest,
    }

    store.register_container_images(service_name, record)

    return {
        "containerImage": record.get("containerImage", {}),
    }

