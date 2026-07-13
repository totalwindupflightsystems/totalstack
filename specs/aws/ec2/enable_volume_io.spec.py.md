---
id: "@specs/aws/ec2/enable_volume_io"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableVolumeIO"
---

# EnableVolumeIO

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_volume_io
> **spec:implements:** @kind:operation EnableVolumeIO
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableVolumeIO.spec.md

Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent.

## Input Shape: EnableVolumeIORequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume. |

## Implementation

```speclang
def enable_volume_io(store, request: dict) -> dict:
    """Enables I/O operations for a volume that had I/O operations disabled because the data on the volume was potentially inconsistent."""
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    resource = store.enable_volume_ios(volume_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource volume_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_volume_ios(volume_id, resource)
    return resource
```
