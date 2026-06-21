---
id: "@specs/aws/lightsail/create_container_service"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateContainerService"
---

# CreateContainerService

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_container_service
> **spec:implements:** @kind:operation CreateContainerService
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateContainerService.spec.md

Creates an Amazon Lightsail container service. A Lightsail container service is a compute resource to which you can deploy containers. For more information, see Container services in Amazon Lightsail in the Lightsail Dev Guide .

## Input Shape: CreateContainerServiceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| deployment | Any  # complex shape |  | An object that describes a deployment for the container service. A deployment specifies the containers that will be laun |
| power | Any  # complex shape | ✓ | The power specification for the container service. The power specifies the amount of memory, vCPUs, and base monthly cos |
| privateRegistryAccess | Any  # complex shape |  | An object to describe the configuration for the container service to access private container image repositories, such a |
| publicDomainNames | Any  # complex shape |  | The public domain names to use with the container service, such as example.com and www.example.com . You can specify up  |
| scale | Any  # complex shape | ✓ | The scale specification for the container service. The scale specifies the allocated compute nodes of the container serv |
| serviceName | Any  # complex shape | ✓ | The name for the container service. The name that you specify for your container service will make up part of its defaul |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the container service during create. Use the TagResource action to tag a reso |

## Output Shape: CreateContainerServiceResult

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
def create_container_service(store, request: dict) -> dict:
    """Creates an Amazon Lightsail container service. A Lightsail container service is a compute resource to which you can deploy containers. For more information, see Container services in Amazon Lightsail """
    power = request.get("power", "").strip() if isinstance(request.get("power"), str) else request.get("power")
    if not power:
        raise ValidationException("power is required")
    scale = request.get("scale", "").strip() if isinstance(request.get("scale"), str) else request.get("scale")
    if not scale:
        raise ValidationException("scale is required")
    service_name = request.get("serviceName", "").strip() if isinstance(request.get("serviceName"), str) else request.get("serviceName")
    if not service_name:
        raise ValidationException("serviceName is required")

    if store.container_services(service_name):
        raise ResourceInUseException(f"Resource service_name already exists")

    record = {
        "serviceName": service_name,
        "power": power,
        "scale": scale,
        "tags": tags,
        "publicDomainNames": public_domain_names,
        "deployment": deployment,
        "privateRegistryAccess": private_registry_access,
    }

    store.container_services(service_name, record)

    return {
        "containerService": record.get("containerService", {}),
    }
```
