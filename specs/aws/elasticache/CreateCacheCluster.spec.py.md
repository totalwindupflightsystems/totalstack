---
id: "@specs/aws/elasticache/CreateCacheCluster"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateCacheCluster

Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached, Valkey or Redis OSS. This operation is not supported for Valkey or Redis OSS (cluster mode enabled) clusters.

## Input Shape: CreateCacheClusterMessage
| Parameter | Type | Required |
|-----------|------|----------|
| CacheClusterId | String | ✓ |
| ReplicationGroupId | String |  |
| AZMode | AZMode |  |
| PreferredAvailabilityZone | String |  |
| PreferredAvailabilityZones | PreferredAvailabilityZoneList |  |
| NumCacheNodes | IntegerOptional |  |
| CacheNodeType | String |  |
| Engine | String |  |
| EngineVersion | String |  |
| CacheParameterGroupName | String |  |
| CacheSubnetGroupName | String |  |
| CacheSecurityGroupNames | CacheSecurityGroupNameList |  |
| SecurityGroupIds | SecurityGroupIdsList |  |
| Tags | TagList |  |
| SnapshotArns | SnapshotArnsList |  |
| SnapshotName | String |  |
| PreferredMaintenanceWindow | String |  |
| Port | IntegerOptional |  |
| NotificationTopicArn | String |  |
| AutoMinorVersionUpgrade | BooleanOptional |  |
| SnapshotRetentionLimit | IntegerOptional |  |
| SnapshotWindow | String |  |
| AuthToken | String |  |
| OutpostMode | OutpostMode |  |
| PreferredOutpostArn | String |  |
| PreferredOutpostArns | PreferredOutpostArnList |  |
| LogDeliveryConfigurations | LogDeliveryConfigurationRequestList |  |
| TransitEncryptionEnabled | BooleanOptional |  |
| NetworkType | NetworkType |  |
| IpDiscovery | IpDiscovery |  |

## Output Shape: CreateCacheClusterResult
- CacheCluster: CacheCluster

## Errors
ReplicationGroupNotFoundFault, InvalidReplicationGroupStateFault, CacheClusterAlreadyExistsFault, InsufficientCacheClusterCapacityFault, CacheSecurityGroupNotFoundFault, CacheSubnetGroupNotFoundFault

## Implementation

```speclang
def create_cache_cluster(store, request):
    """Handle CreateCacheCluster — create a new resource."""
    if "CacheClusterId" not in request or not request["CacheClusterId"]:
        raise InvalidParameterValueException("CacheClusterId is required")
    resource_name = request["CacheClusterId"]
    if resource_name in store.cache_clusters:
        raise CacheClusterAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"
    record.setdefault("Engine", "redis")
    record.setdefault("CacheNodeType", "cache.t2.micro")
    record.setdefault("NumCacheNodes", 1)

    store.cache_clusters[resource_name] = record

    # Build response
    response = {}
    response["CacheClusterId"] = resource_name
    response["Status"] = "available"
    response["CacheNodeType"] = record.get("CacheNodeType", "cache.t2.micro")
    response["Engine"] = record.get("Engine", "redis")
    response["NumCacheNodes"] = record.get("NumCacheNodes", 1)
    return response
```
