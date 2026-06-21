---
id: "@specs/aws/lightsail/update_container_service"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateContainerService"
---

# UpdateContainerService

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_container_service
> **spec:implements:** @kind:operation UpdateContainerService
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateContainerService.spec.md

Updates the configuration of your Amazon Lightsail container service, such as its power, scale, and public domain names.

## Input Shape: UpdateContainerServiceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| isDisabled | Any  # complex shape |  | A Boolean value to indicate whether the container service is disabled. |
| power | Any  # complex shape |  | The power for the container service. The power specifies the amount of memory, vCPUs, and base monthly cost of each node |
| privateRegistryAccess | Any  # complex shape |  | An object to describe the configuration for the container service to access private container image repositories, such a |
| publicDomainNames | Any  # complex shape |  | The public domain names to use with the container service, such as example.com and www.example.com . You can specify up  |
| scale | Any  # complex shape |  | The scale for the container service. The scale specifies the allocated compute nodes of the container service. The power |
| serviceName | Any  # complex shape | ✓ | The name of the container service to update. |

## Output Shape: UpdateContainerServiceResult

- **containerService** (Any  # complex shape): An object that describes a container service.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def update_container_service(store, request: dict) -> dict:
    """Updates the configuration of your Amazon Lightsail container service, such as its power, scale, and public domain names."""
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    resource = store.container_services(service_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource service_name not found")

    # Update mutable fields
    if "power" in request:
        resource["power"] = power
    if "scale" in request:
        resource["scale"] = scale
    if "isDisabled" in request:
        resource["isDisabled"] = is_disabled
    if "publicDomainNames" in request:
        resource["publicDomainNames"] = public_domain_names
    if "privateRegistryAccess" in request:
        resource["privateRegistryAccess"] = private_registry_access

    store.container_services(service_name, resource)
    return resource
```
