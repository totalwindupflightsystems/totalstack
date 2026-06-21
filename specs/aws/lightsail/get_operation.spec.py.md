---
id: "@specs/aws/lightsail/get_operation"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetOperation"
---

# GetOperation

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_operation
> **spec:implements:** @kind:operation GetOperation
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetOperation.spec.md

Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on.

## Input Shape: GetOperationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| operationId | Any  # complex shape | ✓ | A GUID used to identify the operation. |

## Output Shape: GetOperationResult

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
def get_operation(store, request: dict) -> dict:
    """Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on."""
    operation_id = request.get("operationId", "").strip() if isinstance(request.get("operationId"), str) else request.get("operationId")
    if not operation_id:
        raise ValidationException("operationId is required")

    resource = store.operations(operation_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource operation_id not found")
    return {"operationId": operation_id, **resource}
```
