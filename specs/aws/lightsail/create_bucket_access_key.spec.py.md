---
id: "@specs/aws/lightsail/create_bucket_access_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateBucketAccessKey"
---

# CreateBucketAccessKey

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_bucket_access_key
> **spec:implements:** @kind:operation CreateBucketAccessKey
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateBucketAccessKey.spec.md

Creates a new access key for the specified Amazon Lightsail bucket. Access keys consist of an access key ID and corresponding secret access key. Access keys grant full programmatic access to the specified bucket and its objects. You can have a maximum of two access keys per bucket. Use the GetBucketAccessKeys action to get a list of current access keys for a specific bucket. For more information about access keys, see Creating access keys for a bucket in Amazon Lightsail in the Amazon Lightsail Developer Guide . The secretAccessKey value is returned only in response to the CreateBucketAccessKey action. You can get a secret access key only when you first create an access key; you cannot get the secret access key later. If you lose the secret access key, you must create a new access key.

## Input Shape: CreateBucketAccessKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| bucketName | Any  # complex shape | ✓ | The name of the bucket that the new access key will belong to, and grant access to. |

## Output Shape: CreateBucketAccessKeyResult

- **accessKey** (Any  # complex shape): An object that describes the access key that is created.
- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **ServiceException**: A general service exception.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def create_bucket_access_key(store, request: dict) -> dict:
    """Creates a new access key for the specified Amazon Lightsail bucket. Access keys consist of an access key ID and corresponding secret access key. Access keys grant full programmatic access to the speci"""
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")

    if store.bucket_access_keys(bucket_name):
        raise ResourceInUseException(f"Resource bucket_name already exists")

    record = {
        "bucketName": bucket_name,
    }

    store.bucket_access_keys(bucket_name, record)

    return {
        "accessKey": record.get("accessKey", {}),
        "operations": record.get("operations", {}),
    }
```
