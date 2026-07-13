---
id: "@specs/aws/iam/create_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateGroup"
---

# CreateGroup

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_group
> **spec:implements:** @kind:operation CreateGroup
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateGroup.spec.md

Creates a new group. For information about the number of groups you can create, see IAM and STS quotas in the IAM User Guide .

## Input Shape: CreateGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name of the group to create. Do not include the path in this value. IAM user, group, role, and policy names must be  |
| Path | Any  # complex shape |  | The path to the group. For more information about paths, see IAM identifiers in the IAM User Guide . This parameter is o |

## Output Shape: CreateGroupResponse

- **Group** (Any  # complex shape): A structure containing details about the new group.

## Errors
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_group(store, request: dict) -> dict:
    """Creates a new group. For information about the number of groups you can create, see IAM and STS quotas in the IAM User Guide ."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")

    if store.groups(group_name):
        raise ResourceInUseException(f"Resource group_name already exists")

    record = {
        "Path": path,
        "GroupName": group_name,
    }

    store.groups(group_name, record)

    return {
        "Group": record.get("Group", {}),
    }
```
