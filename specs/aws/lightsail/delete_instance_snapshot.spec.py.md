---
id: "@specs/aws/lightsail/delete_instance_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteInstanceSnapshot"
---

# DeleteInstanceSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_instance_snapshot
> **spec:implements:** @kind:operation DeleteInstanceSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteInstanceSnapshot.spec.md

Deletes a specific snapshot of a virtual private server (or instance ). The delete instance snapshot operation supports tag-based access control via resource tags applied to the resource identified by instance snapshot name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteInstanceSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceSnapshotName | Any  # complex shape | ✓ | The name of the snapshot to delete. |

## Output Shape: DeleteInstanceSnapshotResult

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
def delete_instance_snapshot(store, request: dict) -> dict:
    """Deletes a specific snapshot of a virtual private server (or instance ). The delete instance snapshot operation supports tag-based access control via resource tags applied to the resource identified by"""
    instance_snapshot_name = request.get("instanceSnapshotName", "").strip() if isinstance(request.get("instanceSnapshotName"), str) else request.get("instanceSnapshotName")

    if not store.instance_snapshots(instance_snapshot_name):
        raise ResourceNotFoundException(f"Resource instance_snapshot_name not found")
    store.delete_instance_snapshots(instance_snapshot_name)
    return {}
```
