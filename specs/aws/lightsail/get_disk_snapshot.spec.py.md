---
id: "@specs/aws/lightsail/get_disk_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetDiskSnapshot"
---

# GetDiskSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_disk_snapshot
> **spec:implements:** @kind:operation GetDiskSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetDiskSnapshot.spec.md

Returns information about a specific block storage disk snapshot.

## Input Shape: GetDiskSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| diskSnapshotName | Any  # complex shape | ✓ | The name of the disk snapshot ( my-disk-snapshot ). |

## Output Shape: GetDiskSnapshotResult

- **diskSnapshot** (Any  # complex shape): An object containing information about the disk snapshot.

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
def get_disk_snapshot(store, request: dict) -> dict:
    """Returns information about a specific block storage disk snapshot."""
    disk_snapshot_name = request.get("diskSnapshotName", "").strip() if isinstance(request.get("diskSnapshotName"), str) else request.get("diskSnapshotName")
    if not disk_snapshot_name:
        raise ValidationException("diskSnapshotName is required")

    resource = store.disk_snapshots(disk_snapshot_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource disk_snapshot_name not found")
    return {"diskSnapshotName": disk_snapshot_name, **resource}
```
