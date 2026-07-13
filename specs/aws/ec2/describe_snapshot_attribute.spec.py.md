---
id: "@specs/aws/ec2/describe_snapshot_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeSnapshotAttribute"
---

# DescribeSnapshotAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_snapshot_attribute
> **spec:implements:** @kind:operation DescribeSnapshotAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeSnapshotAttribute.spec.md

Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time. For more information about EBS snapshots, see Amazon EBS snapshots in the Amazon EBS User Guide .

## Input Shape: DescribeSnapshotAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The snapshot attribute you would like to view. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SnapshotId | Any  # complex shape | ✓ | The ID of the EBS snapshot. |

## Output Shape: DescribeSnapshotAttributeResult

- **CreateVolumePermissions** (list[Any  # complex shape]): The users and groups that have the permissions for creating volumes from the snapshot.
- **ProductCodes** (list[Any  # complex shape]): The product codes.
- **SnapshotId** (str): The ID of the EBS snapshot.

## Implementation

```speclang
def describe_snapshot_attribute(store, request: dict) -> dict:
    """Describes the specified attribute of the specified snapshot. You can specify only one attribute at a time. For more information about EBS snapshots, see Amazon EBS snapshots in the Amazon EBS User Gui"""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    resource = store.snapshot_attributes(snapshot_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource snapshot_id not found")
    return {"SnapshotId": snapshot_id, **resource}
```
