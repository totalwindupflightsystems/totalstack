---
id: "@specs/aws/elasticache/DeleteUser"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteUser

For Valkey engine version 7.2 onwards and Redis OSS 6.0 onwards: Deletes a user. The user will be removed from all user groups and in turn removed from all replication groups. For more information, see Using Role Based Access Control (RBAC).

## Input Shape: DeleteUserMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserId | UserId | ✓ |

## Output Shape: User
- UserId: String
- UserName: String
- Status: String
- Engine: EngineType
- MinimumEngineVersion: String
- AccessString: String
- UserGroupIds: UserGroupIdList
- Authentication: Authentication
- ARN: String

## Errors
InvalidUserStateFault, UserNotFoundFault, ServiceLinkedRoleNotFoundFault, InvalidParameterValueException, DefaultUserAssociatedToUserGroupFault

## Implementation

```speclang
def delete_user(store, request):
    """Handle DeleteUser — delete a resource."""
    resource_name = request.get("UserId")
    if not resource_name:
        raise InvalidParameterValueException("UserId is required")
    if resource_name not in store.users:
        raise UserNotFoundFault(f"Resource {resource_name} not found")
    del store.users[resource_name]
    return {}
```
