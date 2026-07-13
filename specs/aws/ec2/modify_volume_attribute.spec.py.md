---
id: "@specs/aws/ec2/modify_volume_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVolumeAttribute"
---

# ModifyVolumeAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_volume_attribute
> **spec:implements:** @kind:operation ModifyVolumeAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVolumeAttribute.spec.md

Modifies a volume attribute. By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data corruption. The I/O access to the volume can be resumed by first enabling I/O access and then checking the data consistency on your volume. You can change the default behavior to resume I/O operations. We recommend that you change this only for boot volumes or for volumes that are stateless or disposable.

## Input Shape: ModifyVolumeAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AutoEnableIO | Any  # complex shape |  | Indicates whether the volume should be auto-enabled for I/O operations. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume. |

## Implementation

```speclang
def modify_volume_attribute(store, request: dict) -> dict:
    """Modifies a volume attribute. By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data """
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    resource = store.volume_attributes(volume_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource volume_id not found")

    # Update mutable fields
    if "AutoEnableIO" in request:
        resource["AutoEnableIO"] = auto_enable_io
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.volume_attributes(volume_id, resource)
    return resource
```
