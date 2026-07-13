---
id: "@specs/aws/ec2/deregister_image"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeregisterImage"
---

# DeregisterImage

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/deregister_image
> **spec:implements:** @kind:operation DeregisterImage
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeregisterImage.spec.md

Deregisters the specified AMI. A deregistered AMI can't be used to launch new instances. If a deregistered EBS-backed AMI matches a Recycle Bin retention rule, it moves to the Recycle Bin for the specified retention period. It can be restored before its retention period expires, after which it is permanently deleted. If the deregistered AMI doesn't match a retention rule, it is permanently deleted immediately. For more information, see Recover deleted Amazon EBS snapshots and EBS-backed AMIs with Recycle Bin in the Amazon EBS User Guide . When deregistering an EBS-backed AMI, you can optionally delete its associated snapshots at the same time. However, if a snapshot is associated with multiple AMIs, it won't be deleted even if specified for deletion, although the AMI will still be deregistered. Deregistering an AMI does not delete the following: Instances already launched from the AMI. You'll continue to incur usage costs for the instances until you terminate them. For EBS-backed AMIs: Snapshots that are associated with multiple AMIs. You'll continue to incur snapshot storage costs. For instance store-backed AMIs: The files uploaded to Amazon S3 during AMI creation. You'll continue to incur S3 storage costs. For more information, see Deregister an Amazon EC2 AMI in the Amazon EC2 User Guide .

## Input Shape: DeregisterImageRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DeleteAssociatedSnapshots | bool |  | Specifies whether to delete the snapshots associated with the AMI during deregistration. If a snapshot is associated wit |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |

## Output Shape: DeregisterImageResult

- **DeleteSnapshotResults** (Any  # complex shape): The deletion result for each snapshot associated with the AMI, including the snapshot ID and its success or error code.
- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def deregister_image(store, request: dict) -> dict:
    """Deregisters the specified AMI. A deregistered AMI can't be used to launch new instances. If a deregistered EBS-backed AMI matches a Recycle Bin retention rule, it moves to the Recycle Bin for the spec"""
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")

    if store.deregister_images(image_id):
        raise ResourceInUseException(f"Resource image_id already exists")

    record = {
        "ImageId": image_id,
        "DeleteAssociatedSnapshots": delete_associated_snapshots,
        "DryRun": dry_run,
    }

    store.deregister_images(image_id, record)

    return {
        "Return": record.get("Return", {}),
        "DeleteSnapshotResults": record.get("DeleteSnapshotResults", {}),
    }
```
