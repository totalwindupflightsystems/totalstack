---
id: "@specs/aws/lightsail/copy_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CopySnapshot"
---

# CopySnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/copy_snapshot
> **spec:implements:** @kind:operation CopySnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CopySnapshot.spec.md

Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manual or automatic snapshot of an instance or a disk from one Amazon Web Services Region to another in Amazon Lightsail. When copying a manual snapshot , be sure to define the source region , source snapshot name , and target snapshot name parameters. When copying an automatic snapshot , be sure to define the source region , source resource name , target snapshot name , and either the restore date or the use latest restorable auto snapshot parameters.

## Input Shape: CopySnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| restoreDate | Any  # complex shape |  | The date of the source automatic snapshot to copy. Use the get auto snapshots operation to identify the dates of the ava |
| sourceRegion | Any  # complex shape | ✓ | The Amazon Web Services Region where the source manual or automatic snapshot is located. |
| sourceResourceName | Any  # complex shape |  | The name of the source instance or disk from which the source automatic snapshot was created. Constraint: Define this pa |
| sourceSnapshotName | Any  # complex shape |  | The name of the source manual snapshot to copy. Constraint: Define this parameter only when copying a manual snapshot as |
| targetSnapshotName | Any  # complex shape | ✓ | The name of the new manual snapshot to be created as a copy. |
| useLatestRestorableAutoSnapshot | Any  # complex shape |  | A Boolean value to indicate whether to use the latest available automatic snapshot of the specified source instance or d |

## Output Shape: CopySnapshotResult

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
def copy_snapshot(store, request: dict) -> dict:
    """Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manua"""
    source_region = request.get("sourceRegion", "").strip() if isinstance(request.get("sourceRegion"), str) else request.get("sourceRegion")
    if not source_region:
        raise ValidationException("sourceRegion is required")
    target_snapshot_name = request.get("targetSnapshotName", "").strip() if isinstance(request.get("targetSnapshotName"), str) else request.get("targetSnapshotName")
    if not target_snapshot_name:
        raise ValidationException("targetSnapshotName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CopySnapshot", request)
```
