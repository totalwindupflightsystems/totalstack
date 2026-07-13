---
id: "@specs/aws/ec2/create_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateImage"
---

# CreateImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_image
> **spec:implements:** @kind:operation CreateImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateImage.spec.md

Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped. If you customized your instance with instance store volumes or Amazon EBS volumes in addition to the root device volume, the new AMI contains block device mapping information for those volumes. When you launch an instance from this new AMI, the instance automatically launches with those additional volumes. The location of the source instance determines where you can create the snapshots of the AMI: If the source instance is in a Region, you must create the snapshots in the same Region as the instance. If the source instance is in a Local Zone, you can create the snapshots in the same Local Zone or in its parent Region. For more information, see Create an Amazon EBS-backed AMI in the Amazon Elastic Compute Cloud User Guide .

## Input Shape: CreateImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| BlockDeviceMappings | list[Any  # complex shape] |  | The block device mappings. When using the CreateImage action: You can't change the volume size using the VolumeSize para |
| Description | str |  | A description for the new image. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| Name | str | ✓ | A name for the new image. Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ) |
| NoReboot | bool |  | Indicates whether or not the instance should be automatically rebooted before creating the image. Specify one of the fol |
| SnapshotLocation | Any  # complex shape |  | Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter. The Ama |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the AMI and snapshots on creation. You can tag the AMI, the snapshots, or both. To tag the AMI, the |

## Output Shape: CreateImageResult

- **ImageId** (str): The ID of the new AMI.

## Implementation

```speclang
def create_image(store, request: dict) -> dict:
    """Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is either running or stopped. If you customized your instance with instance store volumes or Amazon EBS volumes in addition to """
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")

    if store.images(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "TagSpecifications": tag_specifications,
        "SnapshotLocation": snapshot_location,
        "DryRun": dry_run,
        "InstanceId": instance_id,
        "Name": name,
        "Description": description,
        "NoReboot": no_reboot,
        "BlockDeviceMappings": block_device_mappings,
    }

    store.images(instance_id, record)

    return {
        "ImageId": record.get("ImageId", {}),
    }
```
