---
id: "@specs/aws/ec2/create_store_image_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateStoreImageTask"
---

# CreateStoreImageTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_store_image_task
> **spec:implements:** @kind:operation CreateStoreImageTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateStoreImageTask.spec.md

Stores an AMI as a single object in an Amazon S3 bucket. To use this API, you must have the required permissions. For more information, see Permissions for storing and restoring AMIs using S3 in the Amazon EC2 User Guide . For more information, see Store and restore an AMI using S3 in the Amazon EC2 User Guide .

## Input Shape: CreateStoreImageTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Bucket | str | ✓ | The name of the Amazon S3 bucket in which the AMI object will be stored. The bucket must be in the Region in which the r |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape | ✓ | The ID of the AMI. |
| S3ObjectTags | list[Any  # complex shape] |  | The tags to apply to the AMI object that will be stored in the Amazon S3 bucket. |

## Output Shape: CreateStoreImageTaskResult

- **ObjectKey** (str): The name of the stored AMI object in the S3 bucket.

## Implementation

```speclang
def create_store_image_task(store, request: dict) -> dict:
    """Stores an AMI as a single object in an Amazon S3 bucket. To use this API, you must have the required permissions. For more information, see Permissions for storing and restoring AMIs using S3 in the A"""
    bucket = request.get("Bucket", "").strip() if isinstance(request.get("Bucket"), str) else request.get("Bucket")
    if not bucket:
        raise ValidationException("Bucket is required")
    image_id = request.get("ImageId", "").strip() if isinstance(request.get("ImageId"), str) else request.get("ImageId")
    if not image_id:
        raise ValidationException("ImageId is required")

    if store.store_image_tasks(image_id):
        raise ResourceInUseException(f"Resource image_id already exists")

    record = {
        "ImageId": image_id,
        "Bucket": bucket,
        "S3ObjectTags": s3_object_tags,
        "DryRun": dry_run,
    }

    store.store_image_tasks(image_id, record)

    return {
        "ObjectKey": record.get("ObjectKey", {}),
    }
```
