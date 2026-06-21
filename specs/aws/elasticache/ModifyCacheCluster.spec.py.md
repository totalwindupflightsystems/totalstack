---
id: "@specs/aws/elasticache/ModifyCacheCluster"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ModifyCacheCluster

Modifies the settings for a cluster. You can use this operation to change one or more cluster configuration parameters by specifying the parameters and the new values.

## Input Shape: ModifyCacheClusterMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheClusterId | String | ✓ |
| NumCacheNodes | IntegerOptional |  |
| CacheNodeIdsToRemove | CacheNodeIdsList |  |
| AZMode | AZMode |  |
| NewAvailabilityZones | PreferredAvailabilityZoneList |  |
| CacheSecurityGroupNames | CacheSecurityGroupNameList |  |
| SecurityGroupIds | SecurityGroupIdsList |  |
| PreferredMaintenanceWindow | String |  |
| NotificationTopicArn | String |  |
| CacheParameterGroupName | String |  |
| NotificationTopicStatus | String |  |
| ApplyImmediately | Boolean |  |
| Engine | String |  |
| EngineVersion | String |  |
| AutoMinorVersionUpgrade | BooleanOptional |  |
| SnapshotRetentionLimit | IntegerOptional |  |
| SnapshotWindow | String |  |
| CacheNodeType | String |  |
| AuthToken | String |  |
| AuthTokenUpdateStrategy | AuthTokenUpdateStrategyType |  |
| LogDeliveryConfigurations | LogDeliveryConfigurationRequestList |  |
| IpDiscovery | IpDiscovery |  |
| ScaleConfig | ScaleConfig |  |

## Output Shape: ModifyCacheClusterResult
- CacheCluster: CacheCluster

## Errors
InvalidCacheClusterStateFault, InvalidCacheSecurityGroupStateFault, InsufficientCacheClusterCapacityFault, CacheClusterNotFoundFault, NodeQuotaForClusterExceededFault, NodeQuotaForCustomerExceededFault

## Implementation

```speclang
def modify_cache_cluster(store, request):
    """Handle ModifyCacheCluster — modify a resource."""
    resource_name = request.get("CacheClusterId")
    if not resource_name:
        raise InvalidParameterValueException("CacheClusterId is required")
    if resource_name not in store.cache_clusters:
        raise CacheClusterNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.cache_clusters[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["CacheClusterId"] = resource_name
    return response
```
