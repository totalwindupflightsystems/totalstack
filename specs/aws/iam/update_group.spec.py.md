---
id: "@specs/aws/iam/update_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateGroup"
---

# UpdateGroup

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_group
> **spec:implements:** @kind:operation UpdateGroup
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateGroup.spec.md

Updates the name and/or the path of the specified IAM group. You should understand the implications of changing a group's path or name. For more information, see Renaming users and groups in the IAM User Guide . The person making the request (the principal), must have permission to change the role group with the old name and the new name. For example, to change the group named Managers to MGRs , the principal must have a policy that allows them to update both groups. If the principal has permission to update the Managers group, but not the MGRs group, then the update fails. For more information about permissions, see Access management .

## Input Shape: UpdateGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | Name of the IAM group to update. If you're changing the name of the group, this is the original name. This parameter all |
| NewGroupName | Any  # complex shape |  | New name for the IAM group. Only include this if changing the group's name. IAM user, group, role, and policy names must |
| NewPath | Any  # complex shape |  | New path for the IAM group. Only include this if changing the group's path. This parameter allows (through its regex pat |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_group(store, request: dict) -> dict:
    """Updates the name and/or the path of the specified IAM group. You should understand the implications of changing a group's path or name. For more information, see Renaming users and groups in the IAM U"""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")

    resource = store.groups(group_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource group_name not found")

    # Update mutable fields
    if "NewPath" in request:
        resource["NewPath"] = new_path
    if "NewGroupName" in request:
        resource["NewGroupName"] = new_group_name

    store.groups(group_name, resource)
    return resource
```
