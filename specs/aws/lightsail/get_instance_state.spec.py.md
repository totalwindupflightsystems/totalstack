---
id: "@specs/aws/lightsail/get_instance_state"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetInstanceState"
---

# GetInstanceState

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_instance_state
> **spec:implements:** @kind:operation GetInstanceState
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetInstanceState.spec.md

Returns the state of a specific instance. Works on one instance at a time.

## Input Shape: GetInstanceStateRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceName | Any  # complex shape | ✓ | The name of the instance to get state information about. |

## Output Shape: GetInstanceStateResult

- **state** (Any  # complex shape): The state of the instance.

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
def get_instance_state(store, request: dict) -> dict:
    """Returns the state of a specific instance. Works on one instance at a time."""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_states(instance_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_name not found")
    return {"instanceName": instance_name, **resource}
```
