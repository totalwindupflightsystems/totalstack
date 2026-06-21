---
id: "@specs/aws/lightsail/delete_bucket"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteBucket"
---

# DeleteBucket

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_bucket
> **spec:implements:** @kind:operation DeleteBucket
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteBucket.spec.md

Deletes a Amazon Lightsail bucket. When you delete your bucket, the bucket name is released and can be reused for a new bucket in your account or another Amazon Web Services account.

## Input Shape: DeleteBucketRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape | ✓ | The name of the bucket to delete. Use the GetBuckets action to get a list of bucket names that you can specify. |
| forceDelete | Any  # complex shape |  | A Boolean value that indicates whether to force delete the bucket. You must force delete the bucket if it has one of the |

## Output Shape: DeleteBucketResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def delete_bucket(store, request: dict) -> dict:
    """Deletes a Amazon Lightsail bucket. When you delete your bucket, the bucket name is released and can be reused for a new bucket in your account or another Amazon Web Services account."""
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")

    if not store.buckets(bucket_name):
        raise ResourceNotFoundException(f"Resource bucket_name not found")
    store.delete_buckets(bucket_name)
    return {}
```
