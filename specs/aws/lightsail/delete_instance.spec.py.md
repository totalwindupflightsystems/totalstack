---
id: "@specs/aws/lightsail/delete_instance"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteInstance"
---

# DeleteInstance

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_instance
> **spec:implements:** @kind:operation DeleteInstance
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteInstance.spec.md

Deletes an Amazon Lightsail instance. The delete instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteInstanceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| forceDeleteAddOns | Any  # complex shape |  | A Boolean value to indicate whether to delete all add-ons for the instance. |
| instanceName | Any  # complex shape | ✓ | The name of the instance to delete. |

## Output Shape: DeleteInstanceResult

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
def delete_instance(store, request: dict) -> dict:
    """Deletes an Amazon Lightsail instance. The delete instance operation supports tag-based access control via resource tags applied to the resource identified by instance name . For more information, see """
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")

    if not store.instances(instance_name):
        raise ResourceNotFoundException(f"Resource instance_name not found")
    store.delete_instances(instance_name)
    return {}
```
