---
id: "@specs/aws/elasticache/CreateReplicationGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# CreateReplicationGroup

Creates a Valkey or Redis OSS (cluster mode disabled) or a Valkey or Redis OSS (cluster mode enabled) replication group. This API can be used to create a standalone regional replication group or a secondary replication group associated with a Global datastore. A Valkey or Redis OSS (cluster mode disabled) replication group is a collection of nodes, where one of the nodes is a read/write primary and the others are read-only replicas. Writes to the primary are asynchronously propagated to the repl

## Input Shape: CreateReplicationGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ReplicationGroupId | String | ✓ |
| ReplicationGroupDescription | String | ✓ |
| GlobalReplicationGroupId | String |  |
| PrimaryClusterId | String |  |
| AutomaticFailoverEnabled | BooleanOptional |  |
| MultiAZEnabled | BooleanOptional |  |
| NumCacheClusters | IntegerOptional |  |
| PreferredCacheClusterAZs | AvailabilityZonesList |  |
| NumNodeGroups | IntegerOptional |  |
| ReplicasPerNodeGroup | IntegerOptional |  |
| NodeGroupConfiguration | NodeGroupConfigurationList |  |
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
| TransitEncryptionEnabled | BooleanOptional |  |
| AtRestEncryptionEnabled | BooleanOptional |  |
| KmsKeyId | String |  |
| UserGroupIds | UserGroupIdListInput |  |
| LogDeliveryConfigurations | LogDeliveryConfigurationRequestList |  |
| DataTieringEnabled | BooleanOptional |  |
| NetworkType | NetworkType |  |
| IpDiscovery | IpDiscovery |  |
| TransitEncryptionMode | TransitEncryptionMode |  |
| ClusterMode | ClusterMode |  |
| ServerlessCacheSnapshotName | String |  |
| Durability | Durability |  |

## Output Shape: CreateReplicationGroupResult
- ReplicationGroup: ReplicationGroup

## Errors
CacheClusterNotFoundFault, InvalidCacheClusterStateFault, ReplicationGroupAlreadyExistsFault, InvalidUserGroupStateFault, UserGroupNotFoundFault, InsufficientCacheClusterCapacityFault

## Implementation

```speclang
def create_replication_group(store, request):
    """Handle CreateReplicationGroup — create a new resource."""
    if "ReplicationGroupId" not in request or not request["ReplicationGroupId"]:
        raise InvalidParameterValueException("ReplicationGroupId is required")
    if "ReplicationGroupDescription" not in request or not request["ReplicationGroupDescription"]:
        raise InvalidParameterValueException("ReplicationGroupDescription is required")
    resource_name = request["ReplicationGroupId"]
    if resource_name in store.replication_groups:
        raise ReplicationGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"
    record.setdefault("Status", "available")

    store.replication_groups[resource_name] = record

    # Build response
    response = {}
    response["ReplicationGroupId"] = resource_name
    response["Status"] = "available"
    return response
```
