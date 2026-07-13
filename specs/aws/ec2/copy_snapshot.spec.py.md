---
id: "@specs/aws/ec2/copy_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CopySnapshot"
---

# CopySnapshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/copy_snapshot
> **spec:implements:** @kind:operation CopySnapshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CopySnapshot.spec.md

Creates an exact copy of an Amazon EBS snapshot. The location of the source snapshot determines whether you can copy it or not, and the allowed destinations for the snapshot copy. If the source snapshot is in a Region, you can copy it within that Region, to another Region, to an Outpost associated with that Region, or to a Local Zone in that Region. If the source snapshot is in a Local Zone, you can copy it within that Local Zone, to another Local Zone in the same zone group, or to the parent Region of the Local Zone. If the source snapshot is on an Outpost, you can't copy it. When copying snapshots to a Region, the encryption outcome for the snapshot copy depends on the Amazon EBS encryption by default setting for the destination Region, the encryption status of the source snapshot, and the encryption parameters you specify in the request. For more information, see Encryption and snapshot copying . Snapshots copied to an Outpost must be encrypted. Unencrypted snapshots are not supported on Outposts. For more information, Amazon EBS local snapshots on Outposts . Snapshots copies have an arbitrary source volume ID. Do not use this volume ID for any purpose. For more information, see Copy an Amazon EBS snapshot in the Amazon EBS User Guide .

## Input Shape: CopySnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CompletionDurationMinutes | Any  # complex shape |  | Not supported when copying snapshots to or from Local Zones or Outposts. Specify a completion duration, in 15 minute inc |
| Description | str |  | A description for the EBS snapshot. |
| DestinationAvailabilityZone | str |  | The Local Zone, for example, cn-north-1-pkx-1a to which to copy the snapshot. Only supported when copying a snapshot to  |
| DestinationOutpostArn | str |  | The Amazon Resource Name (ARN) of the Outpost to which to copy the snapshot. Only supported when copying a snapshot to a |
| DestinationRegion | str |  | The destination Region to use in the PresignedUrl parameter of a snapshot copy operation. This parameter is only valid f |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Encrypted | bool |  | To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this param |
| KmsKeyId | str |  | The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Ama |
| PresignedUrl | Any  # complex shape |  | When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parame |
| SourceRegion | str | ✓ | The ID of the Region that contains the snapshot to be copied. |
| SourceSnapshotId | str | ✓ | The ID of the EBS snapshot to copy. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the new snapshot. |

## Output Shape: CopySnapshotResult

- **SnapshotId** (str): The ID of the new snapshot.
- **Tags** (list[Any  # complex shape]): Any tags applied to the new snapshot.

## Implementation

```speclang
def copy_snapshot(store, request: dict) -> dict:
    """Creates an exact copy of an Amazon EBS snapshot. The location of the source snapshot determines whether you can copy it or not, and the allowed destinations for the snapshot copy. If the source snapsh"""
    source_region = request.get("SourceRegion", "").strip() if isinstance(request.get("SourceRegion"), str) else request.get("SourceRegion")
    if not source_region:
        raise ValidationException("SourceRegion is required")
    source_snapshot_id = request.get("SourceSnapshotId", "").strip() if isinstance(request.get("SourceSnapshotId"), str) else request.get("SourceSnapshotId")
    if not source_snapshot_id:
        raise ValidationException("SourceSnapshotId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CopySnapshot", request)
```
