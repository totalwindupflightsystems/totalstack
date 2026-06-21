---
id: "@specs/aws/lightsail/get_container_service_powers"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetContainerServicePowers"
---

# GetContainerServicePowers

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_container_service_powers
> **spec:implements:** @kind:operation GetContainerServicePowers
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetContainerServicePowers.spec.md

Returns the list of powers that can be specified for your Amazon Lightsail container services. The power specifies the amount of memory, the number of vCPUs, and the base price of the container service.

## Input Shape: GetContainerServicePowersRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: GetContainerServicePowersResult

- **powers** (list[Any  # complex shape]): An array of objects that describe the powers that can be specified for a container service.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_container_service_powers(store, request: dict) -> dict:
    """Returns the list of powers that can be specified for your Amazon Lightsail container services. The power specifies the amount of memory, the number of vCPUs, and the base price of the container servic"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
