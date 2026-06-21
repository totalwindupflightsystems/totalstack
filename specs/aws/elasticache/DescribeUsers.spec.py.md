---
id: "@specs/aws/elasticache/DescribeUsers"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeUsers

Returns a list of users.

## Input Shape: DescribeUsersMessage
| Parameter | Type | Required |
|-----------|------|----------|
| Engine | EngineType |  |
| UserId | UserId |  |
| Filters | FilterList |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |

## Output Shape: DescribeUsersResult
- Users: UserList
- Marker: String

## Errors
UserNotFoundFault, ServiceLinkedRoleNotFoundFault, InvalidParameterCombinationException

## Implementation

```speclang
def describe_users(store, request):
    """Handle DescribeUsers — describe resources."""
    resource_name = request.get("UserId")
    if resource_name:
        if resource_name not in store.users:
            raise UserNotFoundFault(f"Resource {resource_name} not found")
        return {Users: [dict(store.users[resource_name])]}
    else:
        items = [dict(v) for v in store.users.values()]
        return {Users: items}
```
