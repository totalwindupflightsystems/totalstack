---
id: "@specs/aws/lightsail/create_disk_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateDiskSnapshot"
---

# CreateDiskSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_disk_snapshot
> **spec:implements:** @kind:operation CreateDiskSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateDiskSnapshot.spec.md

Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance. You can take a snapshot of an attached disk that is in use; however, snapshots only capture data that has been written to your disk at the time the snapshot command is issued. This may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the disk long enough to take a snapshot, your snapshot should be complete. Nevertheless, if you cannot pause all file writes to the disk, you should unmount the disk from within the Lightsail instance, issue the create disk snapshot command, and then remount the disk to ensure a consistent and complete snapshot. You may remount and use your disk while the snapshot status is pending. You can also use this operation to create a snapshot of an instance's system volume. You might want to do this, for example, to recover data from the system volume of a botched instance or to create a backup of the system volume like you would for a block storage disk. To create a snapshot of a system volume, just define the instance name parameter when issuing the snapshot command, and a snapshot of the defined instance's system volume will be created. After the snapshot is available, you can create a block storage disk from the snapshot and attach it to a running instance to access the data on the disk. The create disk snapshot operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateDiskSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| diskName | Any  # complex shape |  | The unique name of the source disk ( Disk-Virginia-1 ). This parameter cannot be defined together with the instance name |
| diskSnapshotName | Any  # complex shape | ✓ | The name of the destination disk snapshot ( my-disk-snapshot ) based on the source disk. |
| instanceName | Any  # complex shape |  | The unique name of the source instance ( Amazon_Linux-512MB-Virginia-1 ). When this is defined, a snapshot of the instan |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateDiskSnapshotResult

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
def create_disk_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance. You can take a snapshot of an attach"""
    disk_snapshot_name = request.get("diskSnapshotName", "").strip() if isinstance(request.get("diskSnapshotName"), str) else request.get("diskSnapshotName")
    if not disk_snapshot_name:
        raise ValidationException("diskSnapshotName is required")

    if store.disk_snapshots(disk_snapshot_name):
        raise ResourceInUseException(f"Resource disk_snapshot_name already exists")

    record = {
        "diskName": disk_name,
        "diskSnapshotName": disk_snapshot_name,
        "instanceName": instance_name,
        "tags": tags,
    }

    store.disk_snapshots(disk_snapshot_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
