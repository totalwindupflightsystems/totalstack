---
id: "@specs/aws/lightsail/unpeer_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UnpeerVpc"
---

# UnpeerVpc

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/unpeer_vpc
> **spec:implements:** @kind:operation UnpeerVpc
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UnpeerVpc.spec.md

Unpeers the Lightsail VPC from the user's default VPC.

## Input Shape: UnpeerVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|

## Output Shape: UnpeerVpcResult

- **operation** (Any  # complex shape): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def unpeer_vpc(store, request: dict) -> dict:
    """Unpeers the Lightsail VPC from the user's default VPC."""

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UnpeerVpc", request)
```
