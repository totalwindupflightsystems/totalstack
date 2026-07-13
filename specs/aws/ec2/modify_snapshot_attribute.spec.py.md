---
id: "@specs/aws/ec2/modify_snapshot_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifySnapshotAttribute"
---

# ModifySnapshotAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_snapshot_attribute
> **spec:implements:** @kind:operation ModifySnapshotAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifySnapshotAttribute.spec.md

Adds or removes permission settings for the specified snapshot. You may add or remove specified Amazon Web Services account IDs from a snapshot's list of create volume permissions, but you cannot do both in a single operation. If you need to both add and remove account IDs for a snapshot, you must use multiple operations. You can make up to 500 modifications to a snapshot in a single operation. Encrypted snapshots and snapshots with Amazon Web Services Marketplace product codes cannot be made public. Snapshots encrypted with your default KMS key cannot be shared with other accounts. For more information about modifying snapshot permissions, see Share a snapshot in the Amazon EBS User Guide .

## Input Shape: ModifySnapshotAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape |  | The snapshot attribute to modify. Only volume creation permissions can be modified. |
| CreateVolumePermission | Any  # complex shape |  | A JSON representation of the snapshot attribute modification. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| GroupNames | list[Any  # complex shape] |  | The group to modify for the snapshot. |
| OperationType | Any  # complex shape |  | The type of operation to perform to the attribute. |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot. |
| UserIds | list[str] |  | The account ID to modify for the snapshot. |

## Implementation

```speclang
def modify_snapshot_attribute(store, request: dict) -> dict:
    """Adds or removes permission settings for the specified snapshot. You may add or remove specified Amazon Web Services account IDs from a snapshot's list of create volume permissions, but you cannot do b"""
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    resource = store.snapshot_attributes(snapshot_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource snapshot_id not found")

    # Update mutable fields
    if "Attribute" in request:
        resource["Attribute"] = attribute
    if "CreateVolumePermission" in request:
        resource["CreateVolumePermission"] = create_volume_permission
    if "GroupNames" in request:
        resource["GroupNames"] = group_names
    if "OperationType" in request:
        resource["OperationType"] = operation_type
    if "UserIds" in request:
        resource["UserIds"] = user_ids
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.snapshot_attributes(snapshot_id, resource)
    return resource
```
