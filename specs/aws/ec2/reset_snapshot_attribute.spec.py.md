---
id: "@specs/aws/ec2/reset_snapshot_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ResetSnapshotAttribute"
---

# ResetSnapshotAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reset_snapshot_attribute
> **spec:implements:** @kind:operation ResetSnapshotAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ResetSnapshotAttribute.spec.md

Resets permission settings for the specified snapshot. For more information about modifying snapshot permissions, see Share a snapshot in the Amazon EBS User Guide .

## Input Shape: ResetSnapshotAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The attribute to reset. Currently, only the attribute for permission to create volumes can be reset. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot. |

## Implementation

```speclang
def reset_snapshot_attribute(store, request: dict) -> dict:
    """Resets permission settings for the specified snapshot. For more information about modifying snapshot permissions, see Share a snapshot in the Amazon EBS User Guide ."""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    resource = store.reset_snapshot_attributes(snapshot_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource snapshot_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.reset_snapshot_attributes(snapshot_id, resource)
    return resource
```
