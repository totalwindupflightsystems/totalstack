---
id: "@specs/aws/ec2/lock_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_LockSnapshot"
---

# LockSnapshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/lock_snapshot
> **spec:implements:** @kind:operation LockSnapshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_LockSnapshot.spec.md

Locks an Amazon EBS snapshot in either governance or compliance mode to protect it against accidental or malicious deletions for a specific duration. A locked snapshot can't be deleted. You can also use this action to modify the lock settings for a snapshot that is already locked. The allowed modifications depend on the lock mode and lock state: If the snapshot is locked in governance mode, you can modify the lock mode and the lock duration or lock expiration date. If the snapshot is locked in compliance mode and it is in the cooling-off period, you can modify the lock mode and the lock duration or lock expiration date. If the snapshot is locked in compliance mode and the cooling-off period has lapsed, you can only increase the lock duration or extend the lock expiration date.

## Input Shape: LockSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CoolOffPeriod | Any  # complex shape |  | The cooling-off period during which you can unlock the snapshot or modify the lock settings after locking the snapshot i |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExpirationDate | Any  # complex shape |  | The date and time at which the snapshot lock is to automatically expire, in the UTC time zone ( YYYY-MM-DDThh:mm:ss.sssZ |
| LockDuration | Any  # complex shape |  | The period of time for which to lock the snapshot, in days. The snapshot lock will automatically expire after this perio |
| LockMode | Any  # complex shape | ✓ | The mode in which to lock the snapshot. Specify one of the following: governance - Locks the snapshot in governance mode |
| SnapshotId | Any  # complex shape | ✓ | The ID of the snapshot to lock. |

## Output Shape: LockSnapshotResult

- **CoolOffPeriod** (Any  # complex shape): The compliance mode cooling-off period, in hours.
- **CoolOffPeriodExpiresOn** (Any  # complex shape): The date and time at which the compliance mode cooling-off period expires, in the UTC time zone ( YYYY-MM-DDThh:mm:ss.ss
- **LockCreatedOn** (Any  # complex shape): The date and time at which the snapshot was locked, in the UTC time zone ( YYYY-MM-DDThh:mm:ss.sssZ ).
- **LockDuration** (Any  # complex shape): The period of time for which the snapshot is locked, in days.
- **LockDurationStartTime** (Any  # complex shape): The date and time at which the lock duration started, in the UTC time zone ( YYYY-MM-DDThh:mm:ss.sssZ ).
- **LockExpiresOn** (Any  # complex shape): The date and time at which the lock will expire, in the UTC time zone ( YYYY-MM-DDThh:mm:ss.sssZ ).
- **LockState** (Any  # complex shape): The state of the snapshot lock. Valid states include: compliance-cooloff - The snapshot has been locked in compliance mo
- **SnapshotId** (str): The ID of the snapshot

## Implementation

```speclang
def lock_snapshot(store, request: dict) -> dict:
    """Locks an Amazon EBS snapshot in either governance or compliance mode to protect it against accidental or malicious deletions for a specific duration. A locked snapshot can't be deleted. You can also u"""
    lock_mode = request.get("LockMode", "").strip() if isinstance(request.get("LockMode"), str) else request.get("LockMode")
    if not lock_mode:
        raise ValidationException("LockMode is required")
    snapshot_id = request.get("SnapshotId", "").strip() if isinstance(request.get("SnapshotId"), str) else request.get("SnapshotId")
    if not snapshot_id:
        raise ValidationException("SnapshotId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("LockSnapshot", request)
```
