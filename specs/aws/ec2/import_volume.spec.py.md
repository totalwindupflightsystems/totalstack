---
id: "@specs/aws/ec2/import_volume"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ImportVolume"
---

# ImportVolume

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/import_volume
> **spec:implements:** @kind:operation ImportVolume
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ImportVolume.spec.md

This API action supports only single-volume VMs. To import multi-volume VMs, use ImportImage instead. To import a disk to a snapshot, use ImportSnapshot instead. Creates an import volume task using metadata from the specified disk image. For information about the import manifest referenced by this API action, see VM Import Manifest . This API action is not supported by the Command Line Interface (CLI).

## Input Shape: ImportVolumeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | str |  | The Availability Zone for the resulting EBS volume. Either AvailabilityZone or AvailabilityZoneId must be specified, but |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone for the resulting EBS volume. Either AvailabilityZone or AvailabilityZoneId must be spec |
| Description | str |  | A description of the volume. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Image | Any  # complex shape | ✓ | The disk image. |
| Volume | Any  # complex shape | ✓ | The volume size. |

## Output Shape: ImportVolumeResult

- **ConversionTask** (Any  # complex shape): Information about the conversion task.

## Implementation

```speclang
def import_volume(store, request: dict) -> dict:
    """This API action supports only single-volume VMs. To import multi-volume VMs, use ImportImage instead. To import a disk to a snapshot, use ImportSnapshot instead. Creates an import volume task using me"""
    image = request.get("Image", "").strip() if isinstance(request.get("Image"), str) else request.get("Image")
    if not image:
        raise ValidationException("Image is required")
    volume = request.get("Volume", "").strip() if isinstance(request.get("Volume"), str) else request.get("Volume")
    if not volume:
        raise ValidationException("Volume is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ImportVolume", request)
```
