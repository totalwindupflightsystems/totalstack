---
id: "@specs/aws/lightsail/create_bucket"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateBucket"
---

# CreateBucket

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_bucket
> **spec:implements:** @kind:operation CreateBucket
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateBucket.spec.md

Creates an Amazon Lightsail bucket. A bucket is a cloud storage resource available in the Lightsail object storage service. Use buckets to store objects such as data and its descriptive metadata. For more information about buckets, see Buckets in Amazon Lightsail in the Amazon Lightsail Developer Guide .

## Input Shape: CreateBucketRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape | ✓ | The name for the bucket. For more information about bucket names, see Bucket naming rules in Amazon Lightsail in the Ama |
| bundleId | Any  # complex shape | ✓ | The ID of the bundle to use for the bucket. A bucket bundle specifies the monthly cost, storage space, and data transfer |
| enableObjectVersioning | Any  # complex shape |  | A Boolean value that indicates whether to enable versioning of objects in the bucket. For more information about version |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the bucket during creation. Use the TagResource action to tag the bucket afte |

## Output Shape: CreateBucketResult

- **bucket** (Any  # complex shape): An object that describes the bucket that is created.
- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_bucket(store, request: dict) -> dict:
    """Creates an Amazon Lightsail bucket. A bucket is a cloud storage resource available in the Lightsail object storage service. Use buckets to store objects such as data and its descriptive metadata. For """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")

    if store.buckets(bucket_name):
        raise ResourceInUseException(f"Resource bucket_name already exists")

    record = {
        "bucketName": bucket_name,
        "bundleId": bundle_id,
        "tags": tags,
        "enableObjectVersioning": enable_object_versioning,
    }

    store.buckets(bucket_name, record)

    return {
        "bucket": record.get("bucket", {}),
        "operations": record.get("operations", {}),
    }
```
