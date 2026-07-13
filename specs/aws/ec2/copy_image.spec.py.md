---
id: "@specs/aws/ec2/copy_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CopyImage"
---

# CopyImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/copy_image
> **spec:implements:** @kind:operation CopyImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CopyImage.spec.md

Initiates an AMI copy operation. You must specify the source AMI ID and both the source and destination locations. The copy operation must be initiated in the destination Region. CopyImage supports the following source to destination copies: Region to Region Region to Outpost Parent Region to Local Zone Local Zone to parent Region Between Local Zones with the same parent Region (only supported for certain Local Zones) CopyImage does not support the following source to destination copies: Local Zone to non-parent Regions Between Local Zones with different parent Regions Local Zone to Outpost Outpost to Local Zone Outpost to Region Between Outposts Within same Outpost Cross-partition copies (use CreateStoreImageTask instead) Destination specification Region to Region: The destination Region is the Region in which you initiate the copy operation. Region to Outpost: Specify the destination using the DestinationOutpostArn parameter (the ARN of the Outpost) Region to Local Zone, and Local Zone to Local Zone copies: Specify the destination using the DestinationAvailabilityZone parameter (the name of the destination Local Zone) or DestinationAvailabilityZoneId parameter (the ID of the destination Local Zone). Snapshot encryption Region to Outpost: Backing snapshots copied to an Outpost are encrypted by default using the default encryption key for the Region or the key that you specify. Outposts do not support unencrypted snapshots. Region to Local Zone, and Local Zone to Local Zone: Not all Local Zones require encrypted snapshots. In Local Zones that require encrypted snapshots, backing snapshots are automatically encrypted during copy. In Local Zones where encryption is not required, snapshots retain their original encryption state (encrypted or unencrypted) by default. For more information, including the required permissions for copying an AMI, see Copy an Amazon EC2 AMI in the Amazon EC2 User Guide .

## Input Shape: CopyImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see Ensuring i |
| CopyImageTags | bool |  | Specifies whether to copy your user-defined AMI tags to the new AMI. The following tags are not be copied: System tags ( |
| Description | str |  | A description for the new AMI. |
| DestinationAvailabilityZone | str |  | The Local Zone for the new AMI (for example, cn-north-1-pkx-1a ). Only one of DestinationAvailabilityZone , DestinationA |
| DestinationAvailabilityZoneId | str |  | The ID of the Local Zone for the new AMI (for example, cnn1-pkx1-az1 ). Only one of DestinationAvailabilityZone , Destin |
| DestinationOutpostArn | str |  | The Amazon Resource Name (ARN) of the Outpost for the new AMI. Only specify this parameter when copying an AMI from an A |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Encrypted | bool |  | Specifies whether to encrypt the snapshots of the copied image. You can encrypt a copy of an unencrypted snapshot, but y |
| KmsKeyId | str |  | The identifier of the symmetric Key Management Service (KMS) KMS key to use when creating encrypted volumes. If this par |
| Name | str | ✓ | The name of the new AMI. |
| SnapshotCopyCompletionDurationMinutes | int |  | Specify a completion duration, in 15 minute increments, to initiate a time-based AMI copy. The specified completion dura |
| SourceImageId | str | ✓ | The ID of the AMI to copy. |
| SourceRegion | str | ✓ | The name of the Region that contains the AMI to copy. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the new AMI and new snapshots. You can tag the AMI, the snapshots, or both. To tag the new AMI, the |

## Output Shape: CopyImageResult

- **ImageId** (str): The ID of the new AMI.

## Implementation

```speclang
def copy_image(store, request: dict) -> dict:
    """Initiates an AMI copy operation. You must specify the source AMI ID and both the source and destination locations. The copy operation must be initiated in the destination Region. CopyImage supports th"""
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")
    source_image_id = request.get("SourceImageId", "").strip() if isinstance(request.get("SourceImageId"), str) else request.get("SourceImageId")
    if not source_image_id:
        raise ValidationException("SourceImageId is required")
    source_region = request.get("SourceRegion", "").strip() if isinstance(request.get("SourceRegion"), str) else request.get("SourceRegion")
    if not source_region:
        raise ValidationException("SourceRegion is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CopyImage", request)
```
