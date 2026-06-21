---
id: "@specs/aws/elasticache/DeleteReplicationGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteReplicationGroup

Deletes an existing replication group. By default, this operation deletes the entire replication group, including the primary/primaries and all of the read replicas. If the replication group has only one primary, you can optionally delete only the read replicas, while retaining the primary by setting RetainPrimaryCluster=true. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the selected resources; you cannot cancel or revert this operati

## Input Shape: DeleteReplicationGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ReplicationGroupId | String | ✓ |
| RetainPrimaryCluster | BooleanOptional |  |
| FinalSnapshotIdentifier | String |  |

## Output Shape: DeleteReplicationGroupResult
- ReplicationGroup: ReplicationGroup

## Errors
ReplicationGroupNotFoundFault, InvalidReplicationGroupStateFault, SnapshotAlreadyExistsFault, SnapshotFeatureNotSupportedFault, SnapshotQuotaExceededFault, InvalidParameterValueException

## Implementation

```speclang
def delete_replication_group(store, request):
    """Handle DeleteReplicationGroup — delete a resource."""
    resource_name = request.get("ReplicationGroupId")
    if not resource_name:
        raise InvalidParameterValueException("ReplicationGroupId is required")
    if resource_name not in store.replication_groups:
        raise ReplicationGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.replication_groups[resource_name]
    return {}
```
