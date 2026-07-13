---
id: "@specs/aws/iam/delete_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteGroup"
---

# DeleteGroup

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_group
> **spec:implements:** @kind:operation DeleteGroup
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteGroup.spec.md

Deletes the specified IAM group. The group must not contain any users or have any attached policies.

## Input Shape: DeleteGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the IAM group to delete. This parameter allows (through its regex pattern ) a string of characters consistin |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_group(store, request: dict) -> dict:
    """Deletes the specified IAM group. The group must not contain any users or have any attached policies."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")

    if not store.groups(group_name):
        raise ResourceNotFoundException(f"Resource group_name not found")
    store.delete_groups(group_name)
    return {}
```
