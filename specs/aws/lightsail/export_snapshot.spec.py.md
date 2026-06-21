---
id: "@specs/aws/lightsail/export_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_ExportSnapshot"
---

# ExportSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/export_snapshot
> **spec:implements:** @kind:operation ExportSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_ExportSnapshot.spec.md

Exports an Amazon Lightsail instance or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2). This operation results in an export snapshot record that can be used with the create cloud formation stack operation to create new Amazon EC2 instances. Exported instance snapshots appear in Amazon EC2 as Amazon Machine Images (AMIs), and the instance system disk appears as an Amazon Elastic Block Store (Amazon EBS) volume. Exported disk snapshots appear in Amazon EC2 as Amazon EBS volumes. Snapshots are exported to the same Amazon Web Services Region in Amazon EC2 as the source Lightsail snapshot. The export snapshot operation supports tag-based access control via resource tags applied to the resource identified by source snapshot name . For more information, see the Amazon Lightsail Developer Guide . Use the get instance snapshots or get disk snapshots operations to get a list of snapshots that you can export to Amazon EC2.

## Input Shape: ExportSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| sourceSnapshotName | Any  # complex shape | ✓ | The name of the instance or disk snapshot to be exported to Amazon EC2. |

## Output Shape: ExportSnapshotResult

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
def export_snapshot(store, request: dict) -> dict:
    """Exports an Amazon Lightsail instance or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2). This operation results in an export snapshot record that can be used with the create c"""
    source_snapshot_name = request.get("sourceSnapshotName", "").strip() if isinstance(request.get("sourceSnapshotName"), str) else request.get("sourceSnapshotName")
    if not source_snapshot_name:
        raise ValidationException("sourceSnapshotName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExportSnapshot", request)
```
