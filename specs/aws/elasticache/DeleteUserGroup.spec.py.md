---
id: "@specs/aws/elasticache/DeleteUserGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteUserGroup

For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user group. The user group must first be disassociated from the replication group before it can be deleted. For more information, see Using Role Based Access Control (RBAC).

## Input Shape: DeleteUserGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserGroupId | String | ✓ |

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
UserGroupNotFoundFault, InvalidUserGroupStateFault, ServiceLinkedRoleNotFoundFault, InvalidParameterValueException

## Implementation

```speclang
def delete_user_group(store, request):
    """Handle DeleteUserGroup — delete a resource."""
    resource_name = request.get("UserGroupId")
    if not resource_name:
        raise InvalidParameterValueException("UserGroupId is required")
    if resource_name not in store.user_groups:
        raise UserGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.user_groups[resource_name]
    return {}
```
