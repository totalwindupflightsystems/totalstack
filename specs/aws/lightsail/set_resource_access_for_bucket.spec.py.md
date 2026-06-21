---
id: "@specs/aws/lightsail/set_resource_access_for_bucket"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_SetResourceAccessForBucket"
---

# SetResourceAccessForBucket

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/set_resource_access_for_bucket
> **spec:implements:** @kind:operation SetResourceAccessForBucket
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_SetResourceAccessForBucket.spec.md

Sets the Amazon Lightsail resources that can access the specified Lightsail bucket. Lightsail buckets currently support setting access for Lightsail instances in the same Amazon Web Services Region.

## Input Shape: SetResourceAccessForBucketRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| access | Any  # complex shape | ✓ | The access setting. The following access settings are available: allow - Allows access to the bucket and its objects. de |
| bucketName | Any  # complex shape | ✓ | The name of the bucket for which to set access to another Lightsail resource. |
| resourceName | Any  # complex shape | ✓ | The name of the Lightsail instance for which to set bucket access. The instance must be in a running or stopped state. |

## Output Shape: SetResourceAccessForBucketResult

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
def set_resource_access_for_bucket(store, request: dict) -> dict:
    """Sets the Amazon Lightsail resources that can access the specified Lightsail bucket. Lightsail buckets currently support setting access for Lightsail instances in the same Amazon Web Services Region."""
    access = request.get("access", "").strip() if isinstance(request.get("access"), str) else request.get("access")
    if not access:
        raise ValidationException("access is required")
    bucket_name = request.get("bucketName", "").strip() if isinstance(request.get("bucketName"), str) else request.get("bucketName")
    if not bucket_name:
        raise ValidationException("bucketName is required")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.set_resource_access_for_buckets(resource_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_name not found")

    # Update mutable fields

    store.set_resource_access_for_buckets(resource_name, resource)
    return resource
```
