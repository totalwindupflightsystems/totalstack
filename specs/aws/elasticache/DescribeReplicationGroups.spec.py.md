---
id: "@specs/aws/elasticache/DescribeReplicationGroups"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeReplicationGroups

Returns information about a particular replication group. If no identifier is specified, DescribeReplicationGroups returns information about all replication groups.  This operation is valid for Valkey or Redis OSS only.

## Input Shape: DescribeReplicationGroupsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ReplicationGroupId | String |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |

## Output Shape: ReplicationGroupMessage
- Marker: String
- ReplicationGroups: ReplicationGroupList

## Errors
ReplicationGroupNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def describe_replication_groups(store, request):
    """Handle DescribeReplicationGroups — describe resources."""
    resource_name = request.get("ReplicationGroupId")
    if resource_name:
        if resource_name not in store.replication_groups:
            raise ReplicationGroupNotFoundFault(f"Resource {resource_name} not found")
        return {ReplicationGroups: [dict(store.replication_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.replication_groups.values()]
        return {ReplicationGroups: items}
```
