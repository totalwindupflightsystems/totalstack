---
id: "@specs/aws/iam/update_access_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateAccessKey"
---

# UpdateAccessKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_access_key
> **spec:implements:** @kind:operation UpdateAccessKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateAccessKey.spec.md

Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user's key as part of a key rotation workflow. If the UserName is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. If a temporary access key is used, then UserName is required. If a long-term key is assigned to the user, then UserName is not required. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users. For information about rotating keys, see Managing keys and certificates in the IAM User Guide .

## Input Shape: UpdateAccessKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessKeyId | Any  # complex shape | ✓ | The access key ID of the secret access key you want to update. This parameter allows (through its regex pattern ) a stri |
| Status | Any  # complex shape | ✓ | The status you want to assign to the secret access key. Active means that the key can be used for programmatic calls to  |
| UserName | Any  # complex shape |  | The name of the user whose key you want to update. This parameter allows (through its regex pattern ) a string of charac |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.

## Implementation

```speclang
def update_access_key(store, request: dict) -> dict:
    """Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user's key as part of a key rotation workflow. If the UserName is not spe"""
    access_key_id = request.get("AccessKeyId", "").strip() if isinstance(request.get("AccessKeyId"), str) else request.get("AccessKeyId")
    if not access_key_id:
        raise ValidationException("AccessKeyId is required")
    status = request.get("Status", "").strip() if isinstance(request.get("Status"), str) else request.get("Status")
    if not status:
        raise ValidationException("Status is required")

    resource = store.access_keys(access_key_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource access_key_id not found")

    # Update mutable fields
    if "UserName" in request:
        resource["UserName"] = user_name

    store.access_keys(access_key_id, resource)
    return resource
```
