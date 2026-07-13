---
id: "@specs/aws/ec2/restore_snapshot_from_recycle_bin"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_RestoreSnapshotFromRecycleBin"
---

# RestoreSnapshotFromRecycleBin

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/restore_snapshot_from_recycle_bin
> **spec:implements:** @kind:operation RestoreSnapshotFromRecycleBin
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_RestoreSnapshotFromRecycleBin.spec.md

Restores a snapshot from the Recycle Bin. For more information, see Restore snapshots from the Recycle Bin in the Amazon EBS User Guide .

## Input Shape: RestoreSnapshotFromRecycleBinRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot to restore. |

## Output Shape: RestoreSnapshotFromRecycleBinResult

- **Description** (str): The description for the snapshot.
- **Encrypted** (bool): Indicates whether the snapshot is encrypted.
- **OutpostArn** (str): The ARN of the Outpost on which the snapshot is stored. For more information, see Amazon EBS local snapshots on Outposts
- **OwnerId** (str): The ID of the Amazon Web Services account that owns the EBS snapshot.
- **Progress** (str): The progress of the snapshot, as a percentage.
- **SnapshotId** (str): The ID of the snapshot.
- **SseType** (Any  # complex shape): Reserved for future use.
- **StartTime** (Any  # complex shape): The time stamp when the snapshot was initiated.
- **State** (Any  # complex shape): The state of the snapshot.
- **VolumeId** (str): The ID of the volume that was used to create the snapshot.
- **VolumeSize** (int): The size of the volume, in GiB.

## Implementation

```speclang
def restore_snapshot_from_recycle_bin(store, request: dict) -> dict:
    """Restores a snapshot from the Recycle Bin. For more information, see Restore snapshots from the Recycle Bin in the Amazon EBS User Guide ."""
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("RestoreSnapshotFromRecycleBin", request)
```
