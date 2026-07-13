---
id: "@specs/aws/ec2/modify_snapshot_tier"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifySnapshotTier"
---

# ModifySnapshotTier

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_snapshot_tier
> **spec:implements:** @kind:operation ModifySnapshotTier
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifySnapshotTier.spec.md

Archives an Amazon EBS snapshot. When you archive a snapshot, it is converted to a full snapshot that includes all of the blocks of data that were written to the volume at the time the snapshot was created, and moved from the standard tier to the archive tier. For more information, see Archive Amazon EBS snapshots in the Amazon EBS User Guide .

## Input Shape: ModifySnapshotTierRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot. |
| StorageTier | Any  # complex shape |  | The name of the storage tier. You must specify archive . |

## Output Shape: ModifySnapshotTierResult

- **SnapshotId** (str): The ID of the snapshot.
- **TieringStartTime** (Any  # complex shape): The date and time when the archive process was started.

## Implementation

```speclang
def modify_snapshot_tier(store, request: dict) -> dict:
    """Archives an Amazon EBS snapshot. When you archive a snapshot, it is converted to a full snapshot that includes all of the blocks of data that were written to the volume at the time the snapshot was cr"""
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    resource = store.snapshot_tiers(snapshot_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource snapshot_id not found")

    # Update mutable fields
    if "StorageTier" in request:
        resource["StorageTier"] = storage_tier
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.snapshot_tiers(snapshot_id, resource)
    return resource
```
