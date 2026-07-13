---
id: "@specs/aws/iam/get_user"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetUser"
---

# GetUser

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_user
> **spec:implements:** @kind:operation GetUser
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetUser.spec.md

Retrieves information about the specified IAM user, including the user's creation date, path, unique ID, and ARN. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID used to sign the request to this operation.

## Input Shape: GetUserRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UserName | Any  # complex shape |  | The name of the user to get information about. This parameter is optional. If it is not included, it defaults to the use |

## Output Shape: GetUserResponse

- **User** (Any  # complex shape): A structure containing details about the IAM user. Due to a service issue, password last used data does not include pass

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_user(store, request: dict) -> dict:
    """Retrieves information about the specified IAM user, including the user's creation date, path, unique ID, and ARN. If you do not specify a user name, IAM determines the user name implicitly based on th"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
