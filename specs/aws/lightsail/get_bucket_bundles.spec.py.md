---
id: "@specs/aws/lightsail/get_bucket_bundles"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetBucketBundles"
---

# GetBucketBundles

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_bucket_bundles
> **spec:implements:** @kind:operation GetBucketBundles
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetBucketBundles.spec.md

Returns the bundles that you can apply to a Amazon Lightsail bucket. The bucket bundle specifies the monthly cost, storage quota, and data transfer quota for a bucket. Use the UpdateBucketBundle action to update the bundle for a bucket.

## Input Shape: GetBucketBundlesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| includeInactive | Any  # complex shape |  | A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request. |

## Output Shape: GetBucketBundlesResult

- **bundles** (list[Any  # complex shape]): An object that describes bucket bundles.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_bucket_bundles(store, request: dict) -> dict:
    """Returns the bundles that you can apply to a Amazon Lightsail bucket. The bucket bundle specifies the monthly cost, storage quota, and data transfer quota for a bucket. Use the UpdateBucketBundle actio"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
