---
id: "@specs/aws/ec2/unlock_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UnlockSnapshot"
---

# UnlockSnapshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/unlock_snapshot
> **spec:implements:** @kind:operation UnlockSnapshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UnlockSnapshot.spec.md

Unlocks a snapshot that is locked in governance mode or that is locked in compliance mode but still in the cooling-off period. You can't unlock a snapshot that is locked in compliance mode after the cooling-off period has expired.

## Input Shape: UnlockSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot to unlock. |

## Output Shape: UnlockSnapshotResult

- **SnapshotId** (str): The ID of the snapshot.

## Implementation

```speclang
def unlock_snapshot(store, request: dict) -> dict:
    """Unlocks a snapshot that is locked in governance mode or that is locked in compliance mode but still in the cooling-off period. You can't unlock a snapshot that is locked in compliance mode after the c"""
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("UnlockSnapshot", request)
```
