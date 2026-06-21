---
id: "@specs/aws/lightsail/get_regions"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetRegions"
---

# GetRegions

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_regions
> **spec:implements:** @kind:operation GetRegions
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetRegions.spec.md

Returns a list of all valid regions for Amazon Lightsail. Use the include availability zones parameter to also return the Availability Zones in a region.

## Input Shape: GetRegionsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includeAvailabilityZones | Any  # complex shape |  | A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones ar |
| includeRelationalDatabaseAvailabilityZones | Any  # complex shape |  | A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availab |

## Output Shape: GetRegionsResult

- **regions** (list[Any  # complex shape]): An array of key-value pairs containing information about your get regions request.

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def get_regions(store, request: dict) -> dict:
    """Returns a list of all valid regions for Amazon Lightsail. Use the include availability zones parameter to also return the Availability Zones in a region."""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
