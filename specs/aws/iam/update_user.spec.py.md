---
id: "@specs/aws/iam/update_user"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateUser"
---

# UpdateUser

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_user
> **spec:implements:** @kind:operation UpdateUser
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateUser.spec.md

Updates the name and/or the path of the specified IAM user. You should understand the implications of changing an IAM user's path or name. For more information, see Renaming an IAM user and Renaming an IAM group in the IAM User Guide . To change a user name, the requester must have appropriate permissions on both the source object and the target object. For example, to change Bob to Robert, the entity making the request must have permission on Bob and Robert, or must have permission on all (*). For more information about permissions, see Permissions and policies .

## Input Shape: UpdateUserRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NewPath | Any  # complex shape |  | New path for the IAM user. Include this parameter only if you're changing the user's path. This parameter allows (throug |
| NewUserName | Any  # complex shape |  | New name for the user. Include this parameter only if you're changing the user's name. IAM user, group, role, and policy |
| UserName | Any  # complex shape | ✓ | Name of the user to update. If you're changing the name of the user, this is the original user name. This parameter allo |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **EntityTemporarilyUnmodifiableException**: The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to su
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_user(store, request: dict) -> dict:
    """Updates the name and/or the path of the specified IAM user. You should understand the implications of changing an IAM user's path or name. For more information, see Renaming an IAM user and Renaming a"""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    resource = store.users(user_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource user_name not found")

    # Update mutable fields
    if "NewPath" in request:
        resource["NewPath"] = new_path
    if "NewUserName" in request:
        resource["NewUserName"] = new_user_name

    store.users(user_name, resource)
    return resource
```
