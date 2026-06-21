---
id: "@specs/aws/lightsail/get_instance_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetInstanceSnapshot"
---

# GetInstanceSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_instance_snapshot
> **spec:implements:** @kind:operation GetInstanceSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetInstanceSnapshot.spec.md

Returns information about a specific instance snapshot.

## Input Shape: GetInstanceSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceSnapshotName | Any  # complex shape | ✓ | The name of the snapshot for which you are requesting information. |

## Output Shape: GetInstanceSnapshotResult

- **instanceSnapshot** (Any  # complex shape): An array of key-value pairs containing information about the results of your get instance snapshot request.

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
def get_instance_snapshot(store, request: dict) -> dict:
    """Returns information about a specific instance snapshot."""
    instance_snapshot_name = request.get("instanceSnapshotName", "").strip() if isinstance(request.get("instanceSnapshotName"), str) else request.get("instanceSnapshotName")
    if not instance_snapshot_name:
        raise ValidationException("instanceSnapshotName is required")

    resource = store.instance_snapshots(instance_snapshot_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_snapshot_name not found")
    return {"instanceSnapshotName": instance_snapshot_name, **resource}
```
