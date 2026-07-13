---
id: "@specs/aws/ec2/enable_fast_snapshot_restores"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableFastSnapshotRestores"
---

# EnableFastSnapshotRestores

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_fast_snapshot_restores
> **spec:implements:** @kind:operation EnableFastSnapshotRestores
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableFastSnapshotRestores.spec.md

Enables fast snapshot restores for the specified snapshots in the specified Availability Zones. You get the full benefit of fast snapshot restores after they enter the enabled state. For more information, see Amazon EBS fast snapshot restore in the Amazon EBS User Guide .

## Input Shape: EnableFastSnapshotRestoresRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZoneIds | list[str] |  | One or more Availability Zone IDs. For example, use2-az1 . Either AvailabilityZone or AvailabilityZoneId must be specifi |
| AvailabilityZones | list[str] |  | One or more Availability Zones. For example, us-east-2a . Either AvailabilityZone or AvailabilityZoneId must be specifie |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SourceSnapshotIds | list[Any  # complex shape] | ✓ | The IDs of one or more snapshots. For example, snap-1234567890abcdef0 . You can specify a snapshot that was shared with  |

## Output Shape: EnableFastSnapshotRestoresResult

- **Successful** (Any  # complex shape): Information about the snapshots for which fast snapshot restores were successfully enabled.
- **Unsuccessful** (Any  # complex shape): Information about the snapshots for which fast snapshot restores could not be enabled.

## Implementation

```speclang
def enable_fast_snapshot_restores(store, request: dict) -> dict:
    """Enables fast snapshot restores for the specified snapshots in the specified Availability Zones. You get the full benefit of fast snapshot restores after they enter the enabled state. For more informat"""
    source_snapshot_ids = request.get("SourceSnapshotIds", "").strip() if isinstance(request.get("SourceSnapshotIds"), str) else request.get("SourceSnapshotIds")
    if not source_snapshot_ids:
        raise ValidationException("SourceSnapshotIds is required")

    resource = store.enable_fast_snapshot_restoress(source_snapshot_ids)
    if not resource:
        raise ResourceNotFoundException(f"Resource source_snapshot_ids not found")

    # Update mutable fields
    if "AvailabilityZones" in request:
        resource["AvailabilityZones"] = availability_zones
    if "AvailabilityZoneIds" in request:
        resource["AvailabilityZoneIds"] = availability_zone_ids
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_fast_snapshot_restoress(source_snapshot_ids, resource)
    return resource
```
