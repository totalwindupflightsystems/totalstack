---
id: "@specs/aws/lightsail/delete_bucket_access_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteBucketAccessKey"
---

# DeleteBucketAccessKey

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_bucket_access_key
> **spec:implements:** @kind:operation DeleteBucketAccessKey
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteBucketAccessKey.spec.md

Deletes an access key for the specified Amazon Lightsail bucket. We recommend that you delete an access key if the secret access key is compromised. For more information about access keys, see Creating access keys for a bucket in Amazon Lightsail in the Amazon Lightsail Developer Guide .

## Input Shape: DeleteBucketAccessKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| accessKeyId | Any  # complex shape | ✓ | The ID of the access key to delete. Use the GetBucketAccessKeys action to get a list of access key IDs that you can spec |
| bucketName | Any  # complex shape | ✓ | The name of the bucket that the access key belongs to. |

## Output Shape: DeleteBucketAccessKeyResult

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
def delete_bucket_access_key(store, request: dict) -> dict:
    """Deletes an access key for the specified Amazon Lightsail bucket. We recommend that you delete an access key if the secret access key is compromised. For more information about access keys, see Creatin"""
    access_key_id = request.get("accessKeyId", "").strip() if isinstance(request.get("accessKeyId"), str) else request.get("accessKeyId")
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")

    if not store.bucket_access_keys(bucket_name):
        raise ResourceNotFoundException(f"Resource bucket_name not found")
    store.delete_bucket_access_keys(bucket_name)
    return {}
```
