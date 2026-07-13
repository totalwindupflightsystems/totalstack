---
id: "@specs/aws/ec2/restore_volume_from_recycle_bin"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RestoreVolumeFromRecycleBin"
---

# RestoreVolumeFromRecycleBin

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/restore_volume_from_recycle_bin
> **spec:implements:** @kind:operation RestoreVolumeFromRecycleBin
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RestoreVolumeFromRecycleBin.spec.md

Restores a volume from the Recycle Bin. For more information, see Restore volumes from the Recycle Bin in the Amazon EBS User Guide .

## Input Shape: RestoreVolumeFromRecycleBinRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume to restore. |

## Output Shape: RestoreVolumeFromRecycleBinResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def restore_volume_from_recycle_bin(store, request: dict) -> dict:
    """Restores a volume from the Recycle Bin. For more information, see Restore volumes from the Recycle Bin in the Amazon EBS User Guide ."""
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RestoreVolumeFromRecycleBin", request)
```
