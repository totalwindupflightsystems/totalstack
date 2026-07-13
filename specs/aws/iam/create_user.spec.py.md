---
id: "@specs/aws/iam/create_user"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateUser"
---

# CreateUser

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_user
> **spec:implements:** @kind:operation CreateUser
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateUser.spec.md

Creates a new IAM user for your Amazon Web Services account. For information about quotas for the number of IAM users you can create, see IAM and STS quotas in the IAM User Guide .

## Input Shape: CreateUserRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Path | Any  # complex shape |  | The path for the user name. For more information about paths, see IAM identifiers in the IAM User Guide . This parameter |
| PermissionsBoundary | Any  # complex shape |  | The ARN of the managed policy that is used to set the permissions boundary for the user. A permissions boundary policy d |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the new user. Each tag consists of a key name and an associated value. For mor |
| UserName | Any  # complex shape | ✓ | The name of the user to create. IAM user, group, role, and policy names must be unique within the account. Names are not |

## Output Shape: CreateUserResponse

- **User** (Any  # complex shape): A structure with details about the new IAM user.

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_user(store, request: dict) -> dict:
    """Creates a new IAM user for your Amazon Web Services account. For information about quotas for the number of IAM users you can create, see IAM and STS quotas in the IAM User Guide ."""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    if store.users(user_name):
        raise ResourceInUseException(f"Resource user_name already exists")

    record = {
        "Path": path,
        "UserName": user_name,
        "PermissionsBoundary": permissions_boundary,
        "Tags": tags,
    }

    store.users(user_name, record)

    return {
        "User": record.get("User", {}),
    }
```
