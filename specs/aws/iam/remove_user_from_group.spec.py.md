---
id: "@specs/aws/iam/remove_user_from_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_RemoveUserFromGroup"
---

# RemoveUserFromGroup

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/remove_user_from_group
> **spec:implements:** @kind:operation RemoveUserFromGroup
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_RemoveUserFromGroup.spec.md

Removes the specified user from the specified group.

## Input Shape: RemoveUserFromGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the group to update. This parameter allows (through its regex pattern ) a string of characters consisting of |
| UserName | Any  # complex shape | ✓ | The name of the user to remove. This parameter allows (through its regex pattern ) a string of characters consisting of  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def remove_user_from_group(store, request: dict) -> dict:
    """Removes the specified user from the specified group."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")

    if not store.user_from_groups(group_name):
        raise ResourceNotFoundException(f"Resource group_name not found")
    store.delete_user_from_groups(group_name)
    return {}
```
