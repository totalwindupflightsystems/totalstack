---
id: "@specs/aws/ec2/delete_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSnapshot"
---

# DeleteSnapshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_snapshot
> **spec:implements:** @kind:operation DeleteSnapshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSnapshot.spec.md

Deletes the specified snapshot. When you make periodic snapshots of a volume, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the volume. You cannot delete a snapshot of the root device of an EBS volume used by a registered AMI. You must first deregister the AMI before you can delete the snapshot. For more information, see Delete an Amazon EBS snapshot in the Amazon EBS User Guide .

## Input Shape: DeleteSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SnapshotId | Any  # complex shape | ✓ | The ID of the EBS snapshot. |

## Implementation

```speclang
def delete_snapshot(store, request: dict) -> dict:
    """Deletes the specified snapshot. When you make periodic snapshots of a volume, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in t"""
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")

    if not store.snapshots(snapshot_id):
        raise ResourceNotFoundException(f"Resource snapshot_id not found")
    store.delete_snapshots(snapshot_id)
    return {}
```
