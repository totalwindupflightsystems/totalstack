---
id: "@specs/aws/elasticache/RebootCacheCluster"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# RebootCacheCluster

Reboots some, or all, of the cache nodes within a provisioned cluster. This operation applies any modified cache parameter groups to the cluster. The reboot operation takes place as soon as possible, and results in a momentary outage to the cluster. During the reboot, the cluster status is set to REBOOTING. The reboot causes the contents of the cache (for each cache node being rebooted) to be lost. When the reboot is complete, a cluster event is created. Rebooting a cluster is currently supporte

## Input Shape: RebootCacheClusterMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheClusterId | String | ✓ |
| CacheNodeIdsToReboot | CacheNodeIdsList | ✓ |

## Output Shape: RebootCacheClusterResult
- CacheCluster: CacheCluster

## Errors
InvalidCacheClusterStateFault, CacheClusterNotFoundFault

## Implementation

```speclang
def reboot_cache_cluster(store, request):
    """Handle RebootCacheCluster — reboot cache nodes."""
    resource_name = request.get("CacheClusterId")
    if not resource_name:
        raise InvalidParameterValueException("CacheClusterId is required")
    if resource_name not in store.cache_clusters:
        raise CacheClusterNotFoundFault(f"Cache cluster {resource_name} not found")
    node_ids = request.get("CacheNodeIdsToReboot", [])
    if not node_ids:
        raise InvalidParameterValueException("CacheNodeIdsToReboot is required")
    # Simulate reboot
    return {"CacheClusterId": resource_name, "Status": "rebooting cache cluster nodes"}
```
