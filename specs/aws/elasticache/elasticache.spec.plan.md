---
id: "@specs/aws/elasticache/plan"
version: 1.0.0
target_lang: plan
status: active
owned-by: specs
depends_on:
  - "@specs/aws/elasticache/meta"
---

# ElastiCache Implementation Plan

## Operations (34 core, 75 total)

### Cache Clusters (CRUD)
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateCacheCluster | CacheClusterId | Provision a new cache cluster |
| DescribeCacheClusters | — | List or describe cache clusters |
| DeleteCacheCluster | CacheClusterId | Delete a cache cluster |
| ModifyCacheCluster | CacheClusterId | Modify cluster configuration |
| RebootCacheCluster | CacheClusterId, CacheNodeIdsToReboot | Reboot cache nodes |

### Replication Groups (CRUD)
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateReplicationGroup | ReplicationGroupId, ReplicationGroupDescription | Create a replication group |
| DescribeReplicationGroups | — | List or describe replication groups |
| DeleteReplicationGroup | ReplicationGroupId | Delete a replication group |
| ModifyReplicationGroup | ReplicationGroupId | Modify replication group |

### Cache Parameter Groups
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateCacheParameterGroup | CacheParameterGroupName, CacheParameterGroupFamily, Description | Create parameter group |
| DescribeCacheParameterGroups | — | List parameter groups |
| DeleteCacheParameterGroup | CacheParameterGroupName | Delete parameter group |
| ModifyCacheParameterGroup | CacheParameterGroupName, ParameterNameValues | Modify parameters |

### Cache Subnet Groups
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateCacheSubnetGroup | CacheSubnetGroupName, CacheSubnetGroupDescription, SubnetIds | Create subnet group |
| DescribeCacheSubnetGroups | — | List subnet groups |
| DeleteCacheSubnetGroup | CacheSubnetGroupName | Delete subnet group |
| ModifyCacheSubnetGroup | CacheSubnetGroupName | Modify subnet group |

### Snapshots
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateSnapshot | SnapshotName | Create a snapshot |
| DescribeSnapshots | — | List snapshots |
| DeleteSnapshot | SnapshotName | Delete a snapshot |
| CopySnapshot | SourceSnapshotName, TargetSnapshotName | Copy a snapshot |

### Tags
| Operation | Required | Description |
|-----------|----------|-------------|
| AddTagsToResource | ResourceName, Tags | Add tags to resource |
| ListTagsForResource | ResourceName | List tags on resource |
| RemoveTagsFromResource | ResourceName, TagKeys | Remove tags from resource |

### Users (RBAC)
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateUser | UserId, UserName, Engine, AccessString | Create a user |
| DescribeUsers | — | List users |
| DeleteUser | UserId | Delete a user |
| ModifyUser | UserId | Modify user |

### User Groups
| Operation | Required | Description |
|-----------|----------|-------------|
| CreateUserGroup | UserGroupId, Engine | Create user group |
| DescribeUserGroups | — | List user groups |
| DeleteUserGroup | UserGroupId | Delete user group |
| ModifyUserGroup | UserGroupId | Modify user group |

### Metadata
| Operation | Required | Description |
|-----------|----------|-------------|
| DescribeEvents | — | List service events |
| DescribeCacheEngineVersions | — | List available engine versions |

## Error Model

All errors derive from a common `ElastiCacheException` base. Key error types:

| Error Code | HTTP Status | Meaning |
|-----------|-------------|---------|
| CacheClusterNotFoundFault | 404 | Cache cluster does not exist |
| CacheClusterAlreadyExistsFault | 409 | Cache cluster ID already in use |
| InvalidCacheClusterStateFault | 409 | Operation not valid in current state |
| ReplicationGroupNotFoundFault | 404 | Replication group does not exist |
| ReplicationGroupAlreadyExistsFault | 409 | Replication group ID already in use |
| InvalidReplicationGroupStateFault | 409 | Operation not valid in current state |
| CacheParameterGroupNotFoundFault | 404 | Parameter group does not exist |
| CacheParameterGroupAlreadyExistsFault | 409 | Parameter group name already in use |
| CacheSubnetGroupNotFoundFault | 404 | Subnet group does not exist |
| CacheSubnetGroupAlreadyExistsFault | 409 | Subnet group name already in use |
| SnapshotNotFoundFault | 404 | Snapshot does not exist |
| SnapshotAlreadyExistsFault | 409 | Snapshot name already in use |
| UserNotFoundFault | 404 | User does not exist |
| UserAlreadyExistsFault | 409 | User ID already in use |
| UserGroupNotFoundFault | 404 | User group does not exist |
| UserGroupAlreadyExistsFault | 409 | User group ID already in use |
| TagQuotaPerResourceExceeded | 400 | Too many tags |
| InvalidParameterValueException | 400 | Invalid parameter value |
| InvalidParameterCombinationException | 400 | Conflicting parameters |
| InsufficientCacheClusterCapacityFault | 503 | AWS capacity unavailable |
| NodeQuotaForClusterExceeded | 400 | Too many nodes |
| ServiceLinkedRoleNotFoundFault | 400 | Missing service-linked role |

## Pagination

Describe operations that return lists support:
- `Marker` — pagination token (string)
- `MaxRecords` — page size (int, default 100, max 100)
- Response includes `Marker` for next page when truncated

## Implementation Pattern

Each operation follows the standard handler pattern:
1. **Parse and validate** the request dictionary
2. **Check store** for resource existence, conflicts, state
3. **Perform operation** — create/store, modify, delete
4. **Build response** as a dictionary matching AWS response shape
5. **Return** response dict

For the Query protocol, responses are XML-serialized from the dict representation.
The provider handles XML serialization/deserialization.

## Store Design

```python
class ElastiCacheStore:
    cache_clusters: Dict[str, CacheClusterRecord]
    replication_groups: Dict[str, ReplicationGroupRecord]
    parameter_groups: Dict[str, CacheParameterGroupRecord]
    subnet_groups: Dict[str, CacheSubnetGroupRecord]
    snapshots: Dict[str, SnapshotRecord]
    users: Dict[str, UserRecord]
    user_groups: Dict[str, UserGroupRecord]
    events: List[EventRecord]
    tags: Dict[str, List[TagRecord]]  # resource_arn -> tags
```
