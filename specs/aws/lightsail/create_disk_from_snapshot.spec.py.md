---
id: "@specs/aws/lightsail/create_disk_from_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateDiskFromSnapshot"
---

# CreateDiskFromSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_disk_from_snapshot
> **spec:implements:** @kind:operation CreateDiskFromSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateDiskFromSnapshot.spec.md

Creates a block storage disk from a manual or automatic snapshot of a disk. The resulting disk can be attached to an Amazon Lightsail instance in the same Availability Zone ( us-east-2a ). The create disk from snapshot operation supports tag-based access control via request tags and resource tags applied to the resource identified by disk snapshot name . For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateDiskFromSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| addOns | list[Any  # complex shape] |  | An array of objects that represent the add-ons to enable for the new disk. |
| availabilityZone | Any  # complex shape | ✓ | The Availability Zone where you want to create the disk ( us-east-2a ). Choose the same Availability Zone as the Lightsa |
| diskName | Any  # complex shape | ✓ | The unique Lightsail disk name ( my-disk ). |
| diskSnapshotName | Any  # complex shape |  | The name of the disk snapshot ( my-snapshot ) from which to create the new storage disk. Constraint: This parameter cann |
| restoreDate | Any  # complex shape |  | The date of the automatic snapshot to use for the new disk. Use the get auto snapshots operation to identify the dates o |
| sizeInGb | Any  # complex shape | ✓ | The size of the disk in GB ( 32 ). |
| sourceDiskName | Any  # complex shape |  | The name of the source disk from which the source automatic snapshot was created. Constraints: This parameter cannot be  |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |
| useLatestRestorableAutoSnapshot | Any  # complex shape |  | A Boolean value to indicate whether to use the latest available automatic snapshot. Constraints: This parameter cannot b |

## Output Shape: CreateDiskFromSnapshotResult

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
def create_disk_from_snapshot(store, request: dict) -> dict:
    """Creates a block storage disk from a manual or automatic snapshot of a disk. The resulting disk can be attached to an Amazon Lightsail instance in the same Availability Zone ( us-east-2a ). The create """
    availability_zone = request.get("availabilityZone", "").strip() if isinstance(request.get("availabilityZone"), str) else request.get("availabilityZone")
    if not availability_zone:
        raise ValidationException("availabilityZone is required")
    disk_name = request.get("diskName", "").strip() if isinstance(request.get("diskName"), str) else request.get("diskName")
    if not disk_name:
        raise ValidationException("diskName is required")
    size_in_gb = request.get("sizeInGb", "").strip() if isinstance(request.get("sizeInGb"), str) else request.get("sizeInGb")
    if not size_in_gb:
        raise ValidationException("sizeInGb is required")

    if store.disk_from_snapshots(disk_name):
        raise ResourceInUseException(f"Resource disk_name already exists")

    record = {
        "diskName": disk_name,
        "diskSnapshotName": disk_snapshot_name,
        "availabilityZone": availability_zone,
        "sizeInGb": size_in_gb,
        "tags": tags,
        "addOns": add_ons,
        "sourceDiskName": source_disk_name,
        "restoreDate": restore_date,
        "useLatestRestorableAutoSnapshot": use_latest_restorable_auto_snapshot,
    }

    store.disk_from_snapshots(disk_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
