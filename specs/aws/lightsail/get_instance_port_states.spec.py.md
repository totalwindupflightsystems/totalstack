---
id: "@specs/aws/lightsail/get_instance_port_states"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetInstancePortStates"
---

# GetInstancePortStates

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_instance_port_states
> **spec:implements:** @kind:operation GetInstancePortStates
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetInstancePortStates.spec.md

Returns the firewall port states for a specific Amazon Lightsail instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.

## Input Shape: GetInstancePortStatesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceName | Any  # complex shape | ✓ | The name of the instance for which to return firewall port states. |

## Output Shape: GetInstancePortStatesResult

- **portStates** (list[Any  # complex shape]): An array of objects that describe the firewall port states for the specified instance.

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
def get_instance_port_states(store, request: dict) -> dict:
    """Returns the firewall port states for a specific Amazon Lightsail instance, the IP addresses allowed to connect to the instance through the ports, and the protocol."""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")

    resource = store.instance_port_statess(instance_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_name not found")
    return {"instanceName": instance_name, **resource}
```
