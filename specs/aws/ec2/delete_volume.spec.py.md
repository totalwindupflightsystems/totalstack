---
id: "@specs/aws/ec2/delete_volume"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVolume"
---

# DeleteVolume

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_volume
> **spec:implements:** @kind:operation DeleteVolume
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVolume.spec.md

Deletes the specified EBS volume. The volume must be in the available state (not attached to an instance). The volume can remain in the deleting state for several minutes. For more information, see Delete an Amazon EBS volume in the Amazon EBS User Guide .

## Input Shape: DeleteVolumeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume. |

## Implementation

```speclang
def delete_volume(store, request: dict) -> dict:
    """Deletes the specified EBS volume. The volume must be in the available state (not attached to an instance). The volume can remain in the deleting state for several minutes. For more information, see De"""
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")

    if not store.volumes(volume_id):
        raise ResourceNotFoundException(f"Resource volume_id not found")
    store.delete_volumes(volume_id)
    return {}
```
