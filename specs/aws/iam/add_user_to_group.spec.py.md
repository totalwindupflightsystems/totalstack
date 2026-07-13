---
id: "@specs/aws/iam/add_user_to_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AddUserToGroup"
---

# AddUserToGroup

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/add_user_to_group
> **spec:implements:** @kind:operation AddUserToGroup
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AddUserToGroup.spec.md

Adds the specified user to the specified group.

## Input Shape: AddUserToGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the group to update. This parameter allows (through its regex pattern ) a string of characters consisting of |
| UserName | Any  # complex shape | ✓ | The name of the user to add. This parameter allows (through its regex pattern ) a string of characters consisting of upp |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def add_user_to_group(store, request: dict) -> dict:
    """Adds the specified user to the specified group."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    if store.user_to_groups(group_name):
        raise ResourceInUseException(f"Resource group_name already exists")

    record = {
        "GroupName": group_name,
        "UserName": user_name,
    }

    store.user_to_groups(group_name, record)

    return {
    }
```
