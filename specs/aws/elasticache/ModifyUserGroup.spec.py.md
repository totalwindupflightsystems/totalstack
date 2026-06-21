---
id: "@specs/aws/elasticache/ModifyUserGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ModifyUserGroup

Changes the list of users that belong to the user group.

## Input Shape: ModifyUserGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserGroupId | String | ✓ |
| UserIdsToAdd | UserIdListInput |  |
| UserIdsToRemove | UserIdListInput |  |
| Engine | EngineType |  |

## Output Shape: UserGroup
- UserGroupId: String
- Status: String
- Engine: EngineType
- UserIds: UserIdList
- MinimumEngineVersion: String
- PendingChanges: UserGroupPendingChanges
- ReplicationGroups: UGReplicationGroupIdList
- ServerlessCaches: UGServerlessCacheIdList
- ARN: String

## Errors
UserGroupNotFoundFault, UserNotFoundFault, DuplicateUserNameFault, ServiceLinkedRoleNotFoundFault, DefaultUserRequired, InvalidUserGroupStateFault

## Implementation

```speclang
def modify_user_group(store, request):
    """Handle ModifyUserGroup — modify a resource."""
    resource_name = request.get("UserGroupId")
    if not resource_name:
        raise InvalidParameterValueException("UserGroupId is required")
    if resource_name not in store.user_groups:
        raise UserGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.user_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["UserGroupId"] = resource_name
    return response
```
