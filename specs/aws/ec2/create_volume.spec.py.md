---
id: "@specs/aws/ec2/create_volume"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVolume"
---

# CreateVolume

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_volume
> **spec:implements:** @kind:operation CreateVolume
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVolume.spec.md

Creates an EBS volume that can be attached to an instance in the same Availability Zone. You can create a new empty volume or restore a volume from an EBS snapshot. Any Amazon Web Services Marketplace product codes from the snapshot are propagated to the volume. You can create encrypted volumes. Encrypted volumes must be attached to instances that support Amazon EBS encryption. Volumes that are created from encrypted snapshots are also automatically encrypted. For more information, see Amazon EBS encryption in the Amazon EBS User Guide . You can tag your volumes during creation. For more information, see Tag your Amazon EC2 resources in the Amazon EC2 User Guide . For more information, see Create an Amazon EBS volume in the Amazon EBS User Guide .

## Input Shape: CreateVolumeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | Any  # complex shape |  | The ID of the Availability Zone in which to create the volume. For example, us-east-1a . Either AvailabilityZone or Avai |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone in which to create the volume. For example, use1-az1 . Either AvailabilityZone or Availa |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Encrypted | bool |  | Indicates whether the volume should be encrypted. The effect of setting the encryption state to true depends on the volu |
| Iops | int |  | The number of I/O operations per second (IOPS) to provision for the volume. Required for io1 and io2 volumes. Optional f |
| KmsKeyId | str |  | The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Ama |
| MultiAttachEnabled | bool |  | Indicates whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 I |
| Operator | Any  # complex shape |  | Reserved for internal use. |
| OutpostArn | str |  | The Amazon Resource Name (ARN) of the Outpost on which to create the volume. If you intend to use a volume with an insta |
| Size | int |  | The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the  |
| SnapshotId | Any  # complex shape |  | The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the volume during creation. |
| Throughput | int |  | The throughput to provision for the volume, in MiB/s. Supported for gp3 volumes only. Omit for all other volume types. V |
| VolumeInitializationRate | int |  | Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to  |
| VolumeType | Any  # complex shape |  | The volume type. This parameter can be one of the following values: General Purpose SSD: gp2 | gp3 Provisioned IOPS SSD: |

## Output Shape: Volume

- **Attachments** (list[Any  # complex shape]): This parameter is not returned by CreateVolume. Information about the volume attachments.
- **AvailabilityZone** (str): The Availability Zone for the volume.
- **AvailabilityZoneId** (str): The ID of the Availability Zone for the volume.
- **CreateTime** (Any  # complex shape): The time stamp when volume creation was initiated.
- **Encrypted** (bool): Indicates whether the volume is encrypted.
- **FastRestored** (bool): This parameter is not returned by CreateVolume. Indicates whether the volume was created using fast snapshot restore.
- **Iops** (int): The number of I/O operations per second (IOPS). For gp3 , io1 , and io2 volumes, this represents the number of IOPS that
- **KmsKeyId** (str): The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the volume.
- **MultiAttachEnabled** (bool): Indicates whether Amazon EBS Multi-Attach is enabled.
- **Operator** (Any  # complex shape): The service provider that manages the volume.
- **OutpostArn** (str): The Amazon Resource Name (ARN) of the Outpost.
- **Size** (int): The size of the volume, in GiBs.
- **SnapshotId** (str): The snapshot from which the volume was created, if applicable.
- **SourceVolumeId** (str): The ID of the source volume from which the volume copy was created. Only for volume copies.
- **SseType** (Any  # complex shape): This parameter is not returned by CreateVolume. Reserved for future use.
- **State** (Any  # complex shape): The volume state.
- **Tags** (list[Any  # complex shape]): Any tags assigned to the volume.
- **Throughput** (int): The throughput that the volume supports, in MiB/s.
- **VolumeId** (str): The ID of the volume.
- **VolumeInitializationRate** (int): The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume during c
- **VolumeType** (Any  # complex shape): The volume type.

## Implementation

```speclang
def create_volume(store, request: dict) -> dict:
    """Creates an EBS volume that can be attached to an instance in the same Availability Zone. You can create a new empty volume or restore a volume from an EBS snapshot. Any Amazon Web Services Marketplace"""


    record = {
        "AvailabilityZone": availability_zone,
        "AvailabilityZoneId": availability_zone_id,
        "Encrypted": encrypted,
        "Iops": iops,
        "KmsKeyId": kms_key_id,
        "OutpostArn": outpost_arn,
        "Size": size,
        "SnapshotId": snapshot_id,
        "VolumeType": volume_type,
        "TagSpecifications": tag_specifications,
        "MultiAttachEnabled": multi_attach_enabled,
        "Throughput": throughput,
        "ClientToken": client_token,
        "VolumeInitializationRate": volume_initialization_rate,
        "Operator": operator,
        "DryRun": dry_run,
    }

    store.volumes(record)

    return {
        "AvailabilityZoneId": record.get("AvailabilityZoneId", {}),
        "OutpostArn": record.get("OutpostArn", {}),
        "SourceVolumeId": record.get("SourceVolumeId", {}),
        "Iops": record.get("Iops", {}),
        "Tags": record.get("Tags", {}),
        "VolumeType": record.get("VolumeType", {}),
        "FastRestored": record.get("FastRestored", {}),
        "MultiAttachEnabled": record.get("MultiAttachEnabled", {}),
        "Throughput": record.get("Throughput", {}),
        "SseType": record.get("SseType", {}),
        "Operator": record.get("Operator", {}),
        "VolumeInitializationRate": record.get("VolumeInitializationRate", {}),
        "VolumeId": record.get("VolumeId", {}),
        "Size": record.get("Size", {}),
        "SnapshotId": record.get("SnapshotId", {}),
        "AvailabilityZone": record.get("AvailabilityZone", {}),
        "State": record.get("State", {}),
        "CreateTime": record.get("CreateTime", {}),
        "Attachments": record.get("Attachments", {}),
        "Encrypted": record.get("Encrypted", {}),
        "KmsKeyId": record.get("KmsKeyId", {}),
    }
```
