---
id: "@specs/aws/lightsail/get_bucket_access_keys"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetBucketAccessKeys"
---

# GetBucketAccessKeys

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_bucket_access_keys
> **spec:implements:** @kind:operation GetBucketAccessKeys
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetBucketAccessKeys.spec.md

Returns the existing access key IDs for the specified Amazon Lightsail bucket. This action does not return the secret access key value of an access key. You can get a secret access key only when you create it from the response of the CreateBucketAccessKey action. If you lose the secret access key, you must create a new access key.

## Input Shape: GetBucketAccessKeysRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape | ✓ | The name of the bucket for which to return access keys. |

## Output Shape: GetBucketAccessKeysResult

- **accessKeys** (list[Any  # complex shape]): An object that describes the access keys for the specified bucket.

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def get_bucket_access_keys(store, request: dict) -> dict:
    """Returns the existing access key IDs for the specified Amazon Lightsail bucket. This action does not return the secret access key value of an access key. You can get a secret access key only when you c"""
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")

    resource = store.bucket_access_keyss(bucket_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource bucket_name not found")
    return {"bucketName": bucket_name, **resource}
```
