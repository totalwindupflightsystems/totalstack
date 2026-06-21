---
id: "@specs/aws/elasticache/DeleteCacheCluster"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DeleteCacheCluster

Deletes a previously provisioned cluster. DeleteCacheCluster deletes all associated cache nodes, node endpoints and the cluster itself. When you receive a successful response from this operation, Amazon ElastiCache immediately begins deleting the cluster; you cannot cancel or revert this operation. This operation is not valid for:   Valkey or Redis OSS (cluster mode enabled) clusters   Valkey or Redis OSS (cluster mode disabled) clusters   A cluster that is the last read replica of a replication

## Input Shape: DeleteCacheClusterMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheClusterId | String | ✓ |
| FinalSnapshotIdentifier | String |  |

## Output Shape: DeleteCacheClusterResult
- CacheCluster: CacheCluster

## Errors
CacheClusterNotFoundFault, InvalidCacheClusterStateFault, SnapshotAlreadyExistsFault, SnapshotFeatureNotSupportedFault, SnapshotQuotaExceededFault, InvalidParameterValueException

## Implementation

```speclang
def delete_cache_cluster(store, request):
    """Handle DeleteCacheCluster — delete a resource."""
    resource_name = request.get("CacheClusterId")
    if not resource_name:
        raise InvalidParameterValueException("CacheClusterId is required")
    if resource_name not in store.cache_clusters:
        raise CacheClusterNotFoundFault(f"Resource {resource_name} not found")
    del store.cache_clusters[resource_name]
    return {}
```
