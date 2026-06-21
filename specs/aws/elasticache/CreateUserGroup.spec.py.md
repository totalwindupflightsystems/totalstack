---
id: "@specs/aws/elasticache/CreateUserGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateUserGroup

For Valkey engine version 7.2 onwards and Redis OSS 6.0 to 7.1: Creates a user group. For more information, see Using Role Based Access Control (RBAC)

## Input Shape: CreateUserGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserGroupId | String | ✓ |
| Engine | EngineType | ✓ |
| UserIds | UserIdListInput |  |
| Tags | TagList |  |

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
UserNotFoundFault, DuplicateUserNameFault, UserGroupAlreadyExistsFault, ServiceLinkedRoleNotFoundFault, DefaultUserRequired, UserGroupQuotaExceededFault

## Implementation

```speclang
def create_user_group(store, request):
    """Handle CreateUserGroup — create a new resource."""
    if "UserGroupId" not in request or not request["UserGroupId"]:
        raise InvalidParameterValueException("UserGroupId is required")
    if "Engine" not in request or not request["Engine"]:
        raise InvalidParameterValueException("Engine is required")
    resource_name = request["UserGroupId"]
    if resource_name in store.user_groups:
        raise UserGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.user_groups[resource_name] = record

    # Build response
    response = {}
    response["UserGroupId"] = resource_name
    response["Status"] = "available"
    return response
```
