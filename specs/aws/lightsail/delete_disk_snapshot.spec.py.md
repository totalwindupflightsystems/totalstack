---
id: "@specs/aws/lightsail/delete_disk_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteDiskSnapshot"
---

# DeleteDiskSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_disk_snapshot
> **spec:implements:** @kind:operation DeleteDiskSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteDiskSnapshot.spec.md

Deletes the specified disk snapshot. When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the disk. The delete disk snapshot operation supports tag-based access control via resource tags applied to the resource identified by disk snapshot name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteDiskSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| diskSnapshotName | Any  # complex shape | ✓ | The name of the disk snapshot you want to delete ( my-disk-snapshot ). |

## Output Shape: DeleteDiskSnapshotResult

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
def delete_disk_snapshot(store, request: dict) -> dict:
    """Deletes the specified disk snapshot. When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved i"""
    disk_snapshot_name = request.get("diskSnapshotName", "").strip() if isinstance(request.get("diskSnapshotName"), str) else request.get("diskSnapshotName")

    if not store.disk_snapshots(disk_snapshot_name):
        raise ResourceNotFoundException(f"Resource disk_snapshot_name not found")
    store.delete_disk_snapshots(disk_snapshot_name)
    return {}
```
