---
id: "@specs/aws/lightsail/get_container_services"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerServices"
---

# GetContainerServices

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_services
> **spec:implements:** @kind:operation GetContainerServices
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerServices.spec.md

Returns information about one or more of your Amazon Lightsail container services.

## Input Shape: GetContainerServicesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| serviceName | Any  # complex shape |  | The name of the container service for which to return information. When omitted, the response includes all of your conta |

## Output Shape: ContainerServicesListResult

- **containerServices** (list[Any  # complex shape]): An array of objects that describe one or more container services.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_services(store, request: dict) -> dict:
    """Returns information about one or more of your Amazon Lightsail container services."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
