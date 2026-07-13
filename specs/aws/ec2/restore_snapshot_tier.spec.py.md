---
id: "@specs/aws/ec2/restore_snapshot_tier"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RestoreSnapshotTier"
---

# RestoreSnapshotTier

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/restore_snapshot_tier
> **spec:implements:** @kind:operation RestoreSnapshotTier
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RestoreSnapshotTier.spec.md

Restores an archived Amazon EBS snapshot for use temporarily or permanently, or modifies the restore period or restore type for a snapshot that was previously temporarily restored. For more information see Restore an archived snapshot and modify the restore period or restore type for a temporarily restored snapshot in the Amazon EBS User Guide .

## Input Shape: RestoreSnapshotTierRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| PermanentRestore | bool |  | Indicates whether to permanently restore an archived snapshot. To permanently restore an archived snapshot, specify true |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot to restore. |
| TemporaryRestoreDays | Any  # complex shape |  | Specifies the number of days for which to temporarily restore an archived snapshot. Required for temporary restores only |

## Output Shape: RestoreSnapshotTierResult

- **IsPermanentRestore** (bool): Indicates whether the snapshot is permanently restored. true indicates a permanent restore. false indicates a temporary 
- **RestoreDuration** (int): For temporary restores only. The number of days for which the archived snapshot is temporarily restored.
- **RestoreStartTime** (Any  # complex shape): The date and time when the snapshot restore process started.
- **SnapshotId** (str): The ID of the snapshot.

## Implementation

```speclang
def restore_snapshot_tier(store, request: dict) -> dict:
    """Restores an archived Amazon EBS snapshot for use temporarily or permanently, or modifies the restore period or restore type for a snapshot that was previously temporarily restored. For more informatio"""
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RestoreSnapshotTier", request)
```
