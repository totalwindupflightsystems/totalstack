---
id: "@specs/aws/ec2/modify_volume"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVolume"
---

# ModifyVolume

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_volume
> **spec:implements:** @kind:operation ModifyVolume
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVolume.spec.md

You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity. If your EBS volume is attached to a current-generation EC2 instance type, you might be able to apply these changes without stopping the instance or detaching the volume from it. For more information about modifying EBS volumes, see Amazon EBS Elastic Volumes in the Amazon EBS User Guide . When you complete a resize operation on your volume, you need to extend the volume's file-system size to take advantage of the new storage capacity. For more information, see Extend the file system . For more information, see Monitor the progress of volume modifications in the Amazon EBS User Guide . With previous-generation instance types, resizing an EBS volume might require detaching and reattaching the volume or stopping and restarting the instance. After you initiate a volume modification, you must wait for that modification to reach the completed state before you can initiate another modification for the same volume. You can modify a volume up to four times within a rolling 24-hour period, as long as the volume is in the in-use or available state, and all previous modifications for that volume are completed . If you exceed this limit, you get an error message that indicates when you can perform your next modification.

## Input Shape: ModifyVolumeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Iops | int |  | The target IOPS rate of the volume. This parameter is valid only for gp3 , io1 , and io2 volumes. The following are the  |
| MultiAttachEnabled | bool |  | Specifies whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 N |
| Size | int |  | The target size of the volume, in GiB. The target volume size must be greater than or equal to the existing size of the  |
| Throughput | int |  | The target throughput of the volume, in MiB/s. This parameter is valid only for gp3 volumes. The maximum value is 2,000. |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume. |
| VolumeType | Any  # complex shape |  | The target EBS volume type of the volume. For more information, see Amazon EBS volume types in the Amazon EBS User Guide |

## Output Shape: ModifyVolumeResult

- **VolumeModification** (Any  # complex shape): Information about the volume modification.

## Implementation

```speclang
def modify_volume(store, request: dict) -> dict:
    """You can modify several parameters of an existing EBS volume, including volume size, volume type, and IOPS capacity. If your EBS volume is attached to a current-generation EC2 instance type, you might """
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    resource = store.volumes(volume_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource volume_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "Size" in request:
        resource["Size"] = size
    if "VolumeType" in request:
        resource["VolumeType"] = volume_type
    if "Iops" in request:
        resource["Iops"] = iops
    if "Throughput" in request:
        resource["Throughput"] = throughput
    if "MultiAttachEnabled" in request:
        resource["MultiAttachEnabled"] = multi_attach_enabled

    store.volumes(volume_id, resource)
    return resource
```
