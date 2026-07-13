---
id: "@specs/aws/iam/create_access_key"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateAccessKey"
---

# CreateAccessKey

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_access_key
> **spec:implements:** @kind:operation CreateAccessKey
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateAccessKey.spec.md

Creates a new Amazon Web Services secret access key and corresponding Amazon Web Services access key ID for the specified user. The default status for new keys is Active . If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials. This is true even if the Amazon Web Services account has no associated users. For information about quotas on the number of keys you can create, see IAM and STS quotas in the IAM User Guide . To ensure the security of your Amazon Web Services account, the secret access key is accessible only during key and user creation. You must save the key (for example, in a text file) if you want to be able to access it again. If a secret key is lost, you can delete the access keys for the associated user and then create new keys.

## Input Shape: CreateAccessKeyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UserName | Any  # complex shape |  | The name of the IAM user that the new key will belong to. This parameter allows (through its regex pattern ) a string of |

## Output Shape: CreateAccessKeyResponse

- **AccessKey** (Any  # complex shape): A structure with details about the access key.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_access_key(store, request: dict) -> dict:
    """Creates a new Amazon Web Services secret access key and corresponding Amazon Web Services access key ID for the specified user. The default status for new keys is Active . If you do not specify a user"""


    record = {
        "UserName": user_name,
    }

    store.access_keys(record)

    return {
        "AccessKey": record.get("AccessKey", {}),
    }
```
