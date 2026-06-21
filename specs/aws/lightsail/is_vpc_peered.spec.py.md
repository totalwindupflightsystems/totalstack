---
id: "@specs/aws/lightsail/is_vpc_peered"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_IsVpcPeered"
---

# IsVpcPeered

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/is_vpc_peered
> **spec:implements:** @kind:operation IsVpcPeered
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_IsVpcPeered.spec.md

Returns a Boolean value indicating whether your Lightsail VPC is peered.

## Input Shape: IsVpcPeeredRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: IsVpcPeeredResult

- **isPeered** (Any  # complex shape): Returns true if the Lightsail VPC is peered; otherwise, false .

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
def is_vpc_peered(store, request: dict) -> dict:
    """Returns a Boolean value indicating whether your Lightsail VPC is peered."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("IsVpcPeered", request)
```
