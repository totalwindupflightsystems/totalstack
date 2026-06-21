---
id: "@specs/aws/elasticache/DescribeUserGroups"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeUserGroups

Returns a list of user groups.

## Input Shape: DescribeUserGroupsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| UserGroupId | String |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |

## Output Shape: DescribeUserGroupsResult
- UserGroups: UserGroupList
- Marker: String

## Errors
UserGroupNotFoundFault, ServiceLinkedRoleNotFoundFault, InvalidParameterCombinationException

## Implementation

```speclang
def describe_user_groups(store, request):
    """Handle DescribeUserGroups — describe resources."""
    resource_name = request.get("UserGroupId")
    if resource_name:
        if resource_name not in store.user_groups:
            raise UserGroupNotFoundFault(f"Resource {resource_name} not found")
        return {UserGroups: [dict(store.user_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.user_groups.values()]
        return {UserGroups: items}
```
