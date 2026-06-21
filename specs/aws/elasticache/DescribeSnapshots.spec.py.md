---
id: "@specs/aws/elasticache/DescribeSnapshots"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeSnapshots

Returns information about cluster or replication group snapshots. By default, DescribeSnapshots lists all of your snapshots; it can optionally describe a single snapshot, or just the snapshots associated with a particular cache cluster.  This operation is valid for Valkey or Redis OSS only.

## Input Shape: DescribeSnapshotsMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ReplicationGroupId | String |  |
| CacheClusterId | String |  |
| SnapshotName | String |  |
| SnapshotSource | String |  |
| Marker | String |  |
| MaxRecords | IntegerOptional |  |
| ShowNodeGroupConfig | BooleanOptional |  |

## Output Shape: DescribeSnapshotsListMessage
- Marker: String
- Snapshots: SnapshotList

## Errors
CacheClusterNotFoundFault, SnapshotNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def describe_snapshots(store, request):
    """Handle DescribeSnapshots — describe resources."""
    resource_name = request.get("SnapshotName")
    if resource_name:
        if resource_name not in store.snapshots:
            raise SnapshotNotFoundFault(f"Resource {resource_name} not found")
        return {Snapshots: [dict(store.snapshots[resource_name])]}
    else:
        items = [dict(v) for v in store.snapshots.values()]
        return {Snapshots: items}
```
