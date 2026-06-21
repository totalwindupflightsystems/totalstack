---
id: "@specs/aws/elasticache/DescribeCacheClusters"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# DescribeCacheClusters

Returns information about all provisioned clusters if no cluster identifier is specified, or about a specific cache cluster if a cluster identifier is supplied. By default, abbreviated information about the clusters is returned. You can use the optional ShowCacheNodeInfo flag to retrieve detailed information about the cache nodes associated with the clusters. These details include the DNS address and port for the cache node endpoint. If the cluster is in the creating state, only cluster-level in

## Input Shape: DescribeCacheClustersMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheClusterId | String |  |
| MaxRecords | IntegerOptional |  |
| Marker | String |  |
| ShowCacheNodeInfo | BooleanOptional |  |
| ShowCacheClustersNotInReplicationGroups | BooleanOptional |  |

## Output Shape: CacheClusterMessage
- Marker: String
- CacheClusters: CacheClusterList

## Errors
CacheClusterNotFoundFault, InvalidParameterValueException, InvalidParameterCombinationException

## Implementation

```speclang
def describe_cache_clusters(store, request):
    """Handle DescribeCacheClusters — describe resources."""
    resource_name = request.get("CacheClusterId")
    if resource_name:
        if resource_name not in store.cache_clusters:
            raise CacheClusterNotFoundFault(f"Resource {resource_name} not found")
        return {CacheClusters: [dict(store.cache_clusters[resource_name])]}
    else:
        items = [dict(v) for v in store.cache_clusters.values()]
        return {CacheClusters: items}
```
