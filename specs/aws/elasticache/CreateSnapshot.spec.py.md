---
id: "@specs/aws/elasticache/CreateSnapshot"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateSnapshot

Creates a copy of an entire cluster or replication group at a specific moment in time.  This operation is valid for Valkey or Redis OSS only.

## Input Shape: CreateSnapshotMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ReplicationGroupId | String |  |
| CacheClusterId | String |  |
| SnapshotName | String | ✓ |
| KmsKeyId | String |  |
| Tags | TagList |  |

## Output Shape: CreateSnapshotResult
- Snapshot: Snapshot

## Errors
SnapshotAlreadyExistsFault, CacheClusterNotFoundFault, ReplicationGroupNotFoundFault, InvalidCacheClusterStateFault, InvalidReplicationGroupStateFault, SnapshotQuotaExceededFault

## Implementation

```speclang
def create_snapshot(store, request):
    """Handle CreateSnapshot — create a new resource."""
    if "SnapshotName" not in request or not request["SnapshotName"]:
        raise InvalidParameterValueException("SnapshotName is required")
    resource_name = request["SnapshotName"]
    if resource_name in store.snapshots:
        raise SnapshotAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.snapshots[resource_name] = record

    # Build response
    response = {}
    response["SnapshotName"] = resource_name
    response["Status"] = "available"
    return response
```
