---
id: "@specs/aws/lightsail/stop_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_StopInstance"
---

# StopInstance

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/stop_instance
> **spec:implements:** @kind:operation StopInstance
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_StopInstance.spec.md

Stops a specific Amazon Lightsail instance that is currently running. When you start a stopped instance, Lightsail assigns a new public IP address to the instance. To use the same IP address after stopping and starting an instance, create a static IP address and attach it to the instance. For more information, see the Amazon Lightsail Developer Guide . The stop instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: StopInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| force | Any  # complex shape |  | When set to True , forces a Lightsail instance that is stuck in a stopping state to stop. Only use the force parameter i |
| instanceName | Any  # complex shape | ✓ | The name of the instance (a virtual private server) to stop. |

## Output Shape: StopInstanceResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

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
def stop_instance(store, request: dict) -> dict:
    """Stops a specific Amazon Lightsail instance that is currently running. When you start a stopped instance, Lightsail assigns a new public IP address to the instance. To use the same IP address after sto"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")

    if not store.instances(instance_name):
        raise ResourceNotFoundException(f"Resource instance_name not found")
    store.delete_instances(instance_name)
    return {}
```
