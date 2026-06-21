---
id: "@specs/aws/lightsail/close_instance_public_ports"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CloseInstancePublicPorts"
---

# CloseInstancePublicPorts

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/close_instance_public_ports
> **spec:implements:** @kind:operation CloseInstancePublicPorts
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CloseInstancePublicPorts.spec.md

Closes ports for a specific Amazon Lightsail instance. The CloseInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CloseInstancePublicPortsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceName | Any  # complex shape | ✓ | The name of the instance for which to close ports. |
| portInfo | Any  # complex shape | ✓ | An object to describe the ports to close for the specified instance. |

## Output Shape: CloseInstancePublicPortsResult

- **operation** (Any  # complex shape): An object that describes the result of the action, such as the status of the request, the timestamp of the request, and 

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
def close_instance_public_ports(store, request: dict) -> dict:
    """Closes ports for a specific Amazon Lightsail instance. The CloseInstancePublicPorts action supports tag-based access control via resource tags applied to the resource identified by instanceName . For """
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    port_info = request.get("portInfo", "").strip() if isinstance(request.get("portInfo"), str) else request.get("portInfo")
    if not port_info:
        raise ValidationException("portInfo is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CloseInstancePublicPorts", request)
```
