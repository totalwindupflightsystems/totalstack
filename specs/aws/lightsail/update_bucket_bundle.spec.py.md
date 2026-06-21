---
id: "@specs/aws/lightsail/update_bucket_bundle"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateBucketBundle"
---

# UpdateBucketBundle

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_bucket_bundle
> **spec:implements:** @kind:operation UpdateBucketBundle
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateBucketBundle.spec.md

Updates the bundle, or storage plan, of an existing Amazon Lightsail bucket. A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket. You can update a bucket's bundle only one time within a monthly Amazon Web Services billing cycle. To determine if you can update a bucket's bundle, use the GetBuckets action. The ableToUpdateBundle parameter in the response will indicate whether you can currently update a bucket's bundle. Update a bucket's bundle if it's consistently going over its storage space or data transfer quota, or if a bucket's usage is consistently in the lower range of its storage space or data transfer quota. Due to the unpredictable usage fluctuations that a bucket might experience, we strongly recommend that you update a bucket's bundle only as a long-term strategy, instead of as a short-term, monthly cost-cutting measure. Choose a bucket bundle that will provide the bucket with ample storage space and data transfer for a long time to come.

## Input Shape: UpdateBucketBundleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape | ✓ | The name of the bucket for which to update the bundle. |
| bundleId | Any  # complex shape | ✓ | The ID of the new bundle to apply to the bucket. Use the GetBucketBundles action to get a list of bundle IDs that you ca |

## Output Shape: UpdateBucketBundleResult

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
def update_bucket_bundle(store, request: dict) -> dict:
    """Updates the bundle, or storage plan, of an existing Amazon Lightsail bucket. A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket. You can update a bucket's """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    bundle_id = request.get("bundleId", "").strip() if isinstance(request.get("bundleId"), str) else request.get("bundleId")
    if not bundle_id:
        raise ValidationException("bundleId is required")

    resource = store.bucket_bundles(bucket_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource bucket_name not found")

    # Update mutable fields

    store.bucket_bundles(bucket_name, resource)
    return resource
```
