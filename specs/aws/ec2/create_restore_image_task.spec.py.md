---
id: "@specs/aws/ec2/create_restore_image_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateRestoreImageTask"
---

# CreateRestoreImageTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_restore_image_task
> **spec:implements:** @kind:operation CreateRestoreImageTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateRestoreImageTask.spec.md

Starts a task that restores an AMI from an Amazon S3 object that was previously created by using CreateStoreImageTask . To use this API, you must have the required permissions. For more information, see Permissions for storing and restoring AMIs using S3 in the Amazon EC2 User Guide . For more information, see Store and restore an AMI using S3 in the Amazon EC2 User Guide .

## Input Shape: CreateRestoreImageTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Bucket | str | ✓ | The name of the Amazon S3 bucket that contains the stored AMI object. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Name | str |  | The name for the restored AMI. The name must be unique for AMIs in the Region for this account. If you do not provide a  |
| ObjectKey | str | ✓ | The name of the stored AMI object in the bucket. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the AMI and snapshots on restoration. You can tag the AMI, the snapshots, or both. To tag the AMI,  |

## Output Shape: CreateRestoreImageTaskResult

- **ImageId** (str): The AMI ID.

## Implementation

```speclang
def create_restore_image_task(store, request: dict) -> dict:
    """Starts a task that restores an AMI from an Amazon S3 object that was previously created by using CreateStoreImageTask . To use this API, you must have the required permissions. For more information, s"""
    bucket = request.get("Bucket", "").strip() if isinstance(request.get("Bucket"), str) else request.get("Bucket")
    if not bucket:
        raise ValidationException("Bucket is required")
    object_key = request.get("ObjectKey", "").strip() if isinstance(request.get("ObjectKey"), str) else request.get("ObjectKey")
    if not object_key:
        raise ValidationException("ObjectKey is required")

    if store.restore_image_tasks(bucket):
        raise ResourceInUseException(f"Resource bucket already exists")

    record = {
        "Bucket": bucket,
        "ObjectKey": object_key,
        "Name": name,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.restore_image_tasks(bucket, record)

    return {
        "ImageId": record.get("ImageId", {}),
    }
```
