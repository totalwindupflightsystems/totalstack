---
id: "@specs/aws/ec2/create_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSnapshot"
---

# CreateSnapshot

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_snapshot
> **spec:implements:** @kind:operation CreateSnapshot
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSnapshot.spec.md

Creates a snapshot of an EBS volume and stores it in Amazon S3. You can use snapshots for backups, to make copies of EBS volumes, and to save data before shutting down an instance. The location of the source EBS volume determines where you can create the snapshot. If the source volume is in a Region, you must create the snapshot in the same Region as the volume. If the source volume is in a Local Zone, you can create the snapshot in the same Local Zone or in its parent Amazon Web Services Region. If the source volume is on an Outpost, you can create the snapshot on the same Outpost or in its parent Amazon Web Services Region. When a snapshot is created, any Amazon Web Services Marketplace product codes that are associated with the source volume are propagated to the snapshot. You can take a snapshot of an attached volume that is in use. However, snapshots only capture data that has been written to your Amazon EBS volume at the time the snapshot command is issued; this might exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the volume long enough to take a snapshot, your snapshot should be complete. However, if you cannot pause all file writes to the volume, you should unmount the volume from within the instance, issue the snapshot command, and then remount the volume to ensure a consistent and complete snapshot. You may remount and use your volume while the snapshot status is pending . When you create a snapshot for an EBS volume that serves as a root device, we recommend that you stop the instance before taking the snapshot. Snapshots that are taken from encrypted volumes are automatically encrypted. Volumes that are created from encrypted snapshots are also automatically encrypted. Your encrypted volumes and any associated snapshots always remain protected. For more information, see Amazon EBS encryption in the Amazon EBS User Guide .

## Input Shape: CreateSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Description | str |  | A description for the snapshot. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Location | Any  # complex shape |  | Only supported for volumes in Local Zones. If the source volume is not in a Local Zone, omit this parameter. To create a |
| OutpostArn | str |  | Only supported for volumes on Outposts. If the source volume is not on an Outpost, omit this parameter. To create the sn |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the snapshot during creation. |
| VolumeId | Any  # complex shape | ✓ | The ID of the Amazon EBS volume. |

## Output Shape: Snapshot

- **AvailabilityZone** (str): The Availability Zone or Local Zone of the snapshot. For example, us-west-1a (Availability Zone) or us-west-2-lax-1a (Lo
- **CompletionDurationMinutes** (Any  # complex shape): Only for snapshot copies created with time-based snapshot copy operations. The completion duration requested for the tim
- **CompletionTime** (Any  # complex shape): The time stamp when the snapshot was completed.
- **DataEncryptionKeyId** (str): The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encr
- **Description** (str): The description for the snapshot.
- **Encrypted** (bool): Indicates whether the snapshot is encrypted.
- **FullSnapshotSizeInBytes** (int): The full size of the snapshot, in bytes. This is not the incremental size of the snapshot. This is the full snapshot siz
- **KmsKeyId** (str): The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the parent volume.
- **OutpostArn** (str): The ARN of the Outpost on which the snapshot is stored. For more information, see Amazon EBS local snapshots on Outposts
- **OwnerAlias** (str): The Amazon Web Services owner alias, from an Amazon-maintained list ( amazon ). This is not the user-configured Amazon W
- **OwnerId** (str): The ID of the Amazon Web Services account that owns the EBS snapshot.
- **Progress** (str): The progress of the snapshot, as a percentage.
- **RestoreExpiryTime** (Any  # complex shape): Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snaps
- **SnapshotId** (str): The ID of the snapshot. Each snapshot receives a unique identifier when it is created.
- **SseType** (Any  # complex shape): Reserved for future use.
- **StartTime** (Any  # complex shape): The time stamp when the snapshot was initiated.
- **State** (Any  # complex shape): The snapshot state.
- **StateMessage** (str): Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper
- **StorageTier** (Any  # complex shape): The storage tier in which the snapshot is stored. standard indicates that the snapshot is stored in the standard snapsho
- **Tags** (list[Any  # complex shape]): Any tags assigned to the snapshot.
- **TransferType** (Any  # complex shape): Only for snapshot copies. Indicates whether the snapshot copy was created with a standard or time-based snapshot copy op
- **VolumeId** (str): The ID of the volume that was used to create the snapshot. Snapshots created by a copy snapshot operation have an arbitr
- **VolumeSize** (int): The size of the volume, in GiB.

## Implementation

```speclang
def create_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of an EBS volume and stores it in Amazon S3. You can use snapshots for backups, to make copies of EBS volumes, and to save data before shutting down an instance. The location of the"""
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    if store.snapshots(volume_id):
        raise ResourceInUseException(f"Resource volume_id already exists")

    record = {
        "Description": description,
        "OutpostArn": outpost_arn,
        "VolumeId": volume_id,
        "TagSpecifications": tag_specifications,
        "Location": location,
        "DryRun": dry_run,
    }

    store.snapshots(volume_id, record)

    return {
        "OwnerAlias": record.get("OwnerAlias", {}),
        "OutpostArn": record.get("OutpostArn", {}),
        "Tags": record.get("Tags", {}),
        "StorageTier": record.get("StorageTier", {}),
        "RestoreExpiryTime": record.get("RestoreExpiryTime", {}),
        "SseType": record.get("SseType", {}),
        "AvailabilityZone": record.get("AvailabilityZone", {}),
        "TransferType": record.get("TransferType", {}),
        "CompletionDurationMinutes": record.get("CompletionDurationMinutes", {}),
        "CompletionTime": record.get("CompletionTime", {}),
        "FullSnapshotSizeInBytes": record.get("FullSnapshotSizeInBytes", {}),
        "SnapshotId": record.get("SnapshotId", {}),
        "VolumeId": volume_id,
        "State": record.get("State", {}),
        "StateMessage": record.get("StateMessage", {}),
        "StartTime": record.get("StartTime", {}),
        "Progress": record.get("Progress", {}),
        "OwnerId": record.get("OwnerId", {}),
        "Description": record.get("Description", {}),
        "VolumeSize": record.get("VolumeSize", {}),
        "Encrypted": record.get("Encrypted", {}),
        "KmsKeyId": record.get("KmsKeyId", {}),
        "DataEncryptionKeyId": record.get("DataEncryptionKeyId", {}),
    }
```
