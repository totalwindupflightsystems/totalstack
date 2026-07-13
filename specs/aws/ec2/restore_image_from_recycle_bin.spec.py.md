---
id: "@specs/aws/ec2/restore_image_from_recycle_bin"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RestoreImageFromRecycleBin"
---

# RestoreImageFromRecycleBin

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/restore_image_from_recycle_bin
> **spec:implements:** @kind:operation RestoreImageFromRecycleBin
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RestoreImageFromRecycleBin.spec.md

Restores an AMI from the Recycle Bin. For more information, see Recover deleted Amazon EBS snapshots and EBS-back AMIs with Recycle Bin in the Amazon EC2 User Guide .

## Input Shape: RestoreImageFromRecycleBinRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI to restore. |

## Output Shape: RestoreImageFromRecycleBinResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def restore_image_from_recycle_bin(store, request: dict) -> dict:
    """Restores an AMI from the Recycle Bin. For more information, see Recover deleted Amazon EBS snapshots and EBS-back AMIs with Recycle Bin in the Amazon EC2 User Guide ."""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RestoreImageFromRecycleBin", request)
```
