---
id: "@specs/aws/lightsail/update_bucket"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_UpdateBucket"
---

# UpdateBucket

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/update_bucket
> **spec:implements:** @kind:operation UpdateBucket
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_UpdateBucket.spec.md

Updates an existing Amazon Lightsail bucket. Use this action to update the configuration of an existing bucket, such as versioning, public accessibility, and the Amazon Web Services accounts that can access the bucket.

## Input Shape: UpdateBucketRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| accessLogConfig | Any  # complex shape |  | An object that describes the access log configuration for the bucket. |
| accessRules | Any  # complex shape |  | An object that sets the public accessibility of objects in the specified bucket. |
| bucketName | Any  # complex shape | ✓ | The name of the bucket to update. |
| cors | Any  # complex shape |  | Sets the cross-origin resource sharing (CORS) configuration for your bucket. If a CORS configuration exists, it is repla |
| readonlyAccessAccounts | list[Any  # complex shape] |  | An array of strings to specify the Amazon Web Services account IDs that can access the bucket. You can give a maximum of |
| versioning | Any  # complex shape |  | Specifies whether to enable or suspend versioning of objects in the bucket. The following options can be specified: Enab |

## Output Shape: UpdateBucketResult

- **bucket** (Any  # complex shape): An object that describes the bucket that is updated.
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
def update_bucket(store, request: dict) -> dict:
    """Updates an existing Amazon Lightsail bucket. Use this action to update the configuration of an existing bucket, such as versioning, public accessibility, and the Amazon Web Services accounts that can """
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")

    resource = store.buckets(bucket_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource bucket_name not found")

    # Update mutable fields
    if "accessRules" in request:
        resource["accessRules"] = access_rules
    if "versioning" in request:
        resource["versioning"] = versioning
    if "readonlyAccessAccounts" in request:
        resource["readonlyAccessAccounts"] = readonly_access_accounts
    if "accessLogConfig" in request:
        resource["accessLogConfig"] = access_log_config
    if "cors" in request:
        resource["cors"] = cors

    store.buckets(bucket_name, resource)
    return resource
```
