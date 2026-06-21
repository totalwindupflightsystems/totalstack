---
id: "@specs/aws/lightsail/delete_container_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteContainerImage"
---

# DeleteContainerImage

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_container_image
> **spec:implements:** @kind:operation DeleteContainerImage
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteContainerImage.spec.md

Deletes a container image that is registered to your Amazon Lightsail container service.

## Input Shape: DeleteContainerImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| image | Any  # complex shape | ✓ | The name of the container image to delete from the container service. Use the GetContainerImages action to get the name  |
| serviceName | Any  # complex shape | ✓ | The name of the container service for which to delete a registered container image. |

## Output Shape: DeleteContainerImageResult


## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def delete_container_image(store, request: dict) -> dict:
    """Deletes a container image that is registered to your Amazon Lightsail container service."""
    image = request.get("image", "").strip() if isinstance(request.get("image"), str) else request.get("image")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")

    if not store.container_images(service_name):
        raise ResourceNotFoundException(f"Resource service_name not found")
    store.delete_container_images(service_name)
    return {}
```
