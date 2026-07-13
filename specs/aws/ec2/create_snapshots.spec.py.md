---
id: "@specs/aws/ec2/create_snapshots"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSnapshots"
---

# CreateSnapshots

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_snapshots
> **spec:implements:** @kind:operation CreateSnapshots
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSnapshots.spec.md

Creates crash-consistent snapshots of multiple EBS volumes attached to an Amazon EC2 instance. Volumes are chosen by specifying an instance. Each volume attached to the specified instance will produce one snapshot that is crash-consistent across the instance. You can include all of the volumes currently attached to the instance, or you can exclude the root volume or specific data (non-root) volumes from the multi-volume snapshot set. The location of the source instance determines where you can create the snapshots. If the source instance is in a Region, you must create the snapshots in the same Region as the instance. If the source instance is in a Local Zone, you can create the snapshots in the same Local Zone or in its parent Amazon Web Services Region. If the source instance is on an Outpost, you can create the snapshots on the same Outpost or in its parent Amazon Web Services Region.

## Input Shape: CreateSnapshotsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CopyTagsFromSource | Any  # complex shape |  | Copies the tags from the specified volume to corresponding snapshot. |
| Description | str |  | A description propagated to every snapshot specified by the instance. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceSpecification | Any  # complex shape | ✓ | The instance to specify which volumes should be included in the snapshots. |
| Location | Any  # complex shape |  | Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter. To crea |
| OutpostArn | str |  | Only supported for instances on Outposts. If the source instance is not on an Outpost, omit this parameter. To create th |
| TagSpecifications | list[Any  # complex shape] |  | Tags to apply to every snapshot specified by the instance. |

## Output Shape: CreateSnapshotsResult

- **Snapshots** (Any  # complex shape): List of snapshots.

## Implementation

```speclang
def create_snapshots(store, request: dict) -> dict:
    """Creates crash-consistent snapshots of multiple EBS volumes attached to an Amazon EC2 instance. Volumes are chosen by specifying an instance. Each volume attached to the specified instance will produce"""
    instance_specification = request.get("InstanceSpecification", "").strip() if isinstance(request.get("InstanceSpecification"), str) else request.get("InstanceSpecification")
    if not instance_specification:
        raise ValidationException("InstanceSpecification is required")

    if store.snapshotss(instance_specification):
        raise ResourceInUseException(f"Resource instance_specification already exists")

    record = {
        "Description": description,
        "InstanceSpecification": instance_specification,
        "OutpostArn": outpost_arn,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "CopyTagsFromSource": copy_tags_from_source,
        "Location": location,
    }

    store.snapshotss(instance_specification, record)

    return {
        "Snapshots": record.get("Snapshots", {}),
    }
```
