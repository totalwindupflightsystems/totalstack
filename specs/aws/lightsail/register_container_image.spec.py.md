---
id: "@specs/aws/lightsail/register_container_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_RegisterContainerImage"
---

# RegisterContainerImage

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/register_container_image
> **spec:implements:** @kind:operation RegisterContainerImage
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_RegisterContainerImage.spec.md

Registers a container image to your Amazon Lightsail container service. This action is not required if you install and use the Lightsail Control (lightsailctl) plugin to push container images to your Lightsail container service. For more information, see Pushing and managing container images on your Amazon Lightsail container services in the Amazon Lightsail Developer Guide .

## Input Shape: RegisterContainerImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| digest | Any  # complex shape | ✓ | The digest of the container image to be registered. |
| label | Any  # complex shape | ✓ | The label for the container image when it's registered to the container service. Use a descriptive label that you can us |
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to register a container image. |

## Output Shape: RegisterContainerImageResult

- **containerImage** (Any  # complex shape): An object that describes a container image that is registered to a Lightsail container service

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
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
        raise ResourceInUseException(f"Resource service_name already exists")

    record = {
        "serviceName": service_name,
        "label": label,
        "digest": digest,
    }

    store.register_container_images(service_name, record)

    return {
        "containerImage": record.get("containerImage", {}),
    }
```
