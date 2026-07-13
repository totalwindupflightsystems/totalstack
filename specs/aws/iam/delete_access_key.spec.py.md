---
id: "@specs/aws/iam/delete_access_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteAccessKey"
---

# DeleteAccessKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_access_key
> **spec:implements:** @kind:operation DeleteAccessKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteAccessKey.spec.md

Deletes the access key pair associated with the specified IAM user. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.

## Input Shape: DeleteAccessKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AccessKeyId | Any  # complex shape | ✓ | The access key ID for the access key ID and secret access key you want to delete. This parameter allows (through its reg |
| UserName | Any  # complex shape |  | The name of the user whose access key pair you want to delete. This parameter allows (through its regex pattern ) a stri |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_access_key(store, request: dict) -> dict:
    """Deletes the access key pair associated with the specified IAM user. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing th"""
    access_key_id = request.get("AccessKeyId", "").strip() if isinstance(request.get("AccessKeyId"), str) else request.get("AccessKeyId")

    if not store.access_keys(access_key_id):
        raise ResourceNotFoundException(f"Resource access_key_id not found")
    store.delete_access_keys(access_key_id)
    return {}
```
