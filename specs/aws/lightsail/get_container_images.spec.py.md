---
id: "@specs/aws/lightsail/get_container_images"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerImages"
---

# GetContainerImages

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_images
> **spec:implements:** @kind:operation GetContainerImages
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerImages.spec.md

Returns the container images that are registered to your Amazon Lightsail container service. If you created a deployment on your Lightsail container service that uses container images from a public registry like Docker Hub, those images are not returned as part of this action. Those images are not registered to your Lightsail container service.

## Input Shape: GetContainerImagesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to return registered container images. |

## Output Shape: GetContainerImagesResult

- **containerImages** (list[Any  # complex shape]): An array of objects that describe container images that are registered to the container service.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_images(store, request: dict) -> dict:
    """Returns the container images that are registered to your Amazon Lightsail container service. If you created a deployment on your Lightsail container service that uses container images from a public re"""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_imagess(service_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_name not found")
    return {"serviceName": service_name, **resource}
```
