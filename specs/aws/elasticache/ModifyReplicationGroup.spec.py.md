---
id: "@specs/aws/elasticache/ModifyReplicationGroup"
version: 1.0.0
target_lang: py
status: active
owned-by: codegen
model_pool: code-gen
depends_on:
  - "@specs/aws/elasticache/meta"
  - "@specs/aws/elasticache/plan"
---

# ModifyReplicationGroup

Modifies the settings for a replication group. This is limited to Valkey and Redis OSS 7 and above.    Scaling for Valkey or Redis OSS (cluster mode enabled) in the ElastiCache User Guide    ModifyReplicationGroupShardConfiguration in the ElastiCache API Reference    This operation is valid for Valkey or Redis OSS only.

## Input Shape: ModifyReplicationGroupMessage
| Parameter | Type | Required |
|-----------|------|----------|
| ReplicationGroupId | String | ✓ |
| ReplicationGroupDescription | String |  |
| PrimaryClusterId | String |  |
| SnapshottingClusterId | String |  |
| AutomaticFailoverEnabled | BooleanOptional |  |
| MultiAZEnabled | BooleanOptional |  |
| NodeGroupId | String |  |
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
| UserGroupIdsToAdd | UserGroupIdList |  |
| UserGroupIdsToRemove | UserGroupIdList |  |
| RemoveUserGroups | BooleanOptional |  |
| LogDeliveryConfigurations | LogDeliveryConfigurationRequestList |  |
| IpDiscovery | IpDiscovery |  |
| TransitEncryptionEnabled | BooleanOptional |  |
| TransitEncryptionMode | TransitEncryptionMode |  |
| ClusterMode | ClusterMode |  |
| Durability | Durability |  |

## Output Shape: ModifyReplicationGroupResult
- ReplicationGroup: ReplicationGroup

## Errors
ReplicationGroupNotFoundFault, InvalidReplicationGroupStateFault, InvalidUserGroupStateFault, UserGroupNotFoundFault, InvalidCacheClusterStateFault, InvalidCacheSecurityGroupStateFault

## Implementation

```speclang
def modify_replication_group(store, request):
    """Handle ModifyReplicationGroup — modify a resource."""
    resource_name = request.get("ReplicationGroupId")
    if not resource_name:
        raise InvalidParameterValueException("ReplicationGroupId is required")
    if resource_name not in store.replication_groups:
        raise ReplicationGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.replication_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["ReplicationGroupId"] = resource_name
    return response
```
