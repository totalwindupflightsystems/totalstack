---
id: "@specs/aws/neptune/plan"
version: 1.0.0
target_lang: plan
owned-by: specwriter
status: active
depends_on:
  - "@specs/aws/neptune/meta"
---

# Amazon Neptune — Implementation Plan

## Phase 1: Core CRUD (Complete)
28 handlers across 7 entity types + tags + engine versions:

### DBCluster (4 ops)
- `CreateDBCluster` — validate identifier, engine, create cluster record
- `DeleteDBCluster` — validate state, remove from store
- `ModifyDBCluster` — update mutable fields
- `DescribeDBClusters` — list by identifier or all

### DBInstance (5 ops)
- `CreateDBInstance` — validate class/engine/cluster, create instance, add to cluster members
- `DeleteDBInstance` — validate state, remove from store
- `ModifyDBInstance` — update mutable fields
- `DescribeDBInstances` — list by identifier or all
- `RebootDBInstance` — set status to rebooting

### DBClusterParameterGroup (5 ops)
- `CreateDBClusterParameterGroup` — validate name/family/description
- `DeleteDBClusterParameterGroup` — remove from store
- `ModifyDBClusterParameterGroup` — validate and apply parameters
- `DescribeDBClusterParameterGroups` — list
- `DescribeDBClusterParameters` — return default Neptune parameters

### DBParameterGroup (4 ops)
- `CreateDBParameterGroup` — validate name/family/description
- `DeleteDBParameterGroup` — remove from store
- `ModifyDBParameterGroup` — validate and apply parameters
- `DescribeDBParameterGroups` — list
- `DescribeDBParameters` — return default Neptune parameters

### DBClusterSnapshot (3 ops)
- `CreateDBClusterSnapshot` — validate cluster exists, create snapshot
- `DeleteDBClusterSnapshot` — remove from store
- `DescribeDBClusterSnapshots` — list by cluster/snapshot type

### DBSubnetGroup (3 ops)
- `CreateDBSubnetGroup` — validate >= 2 subnets across AZs
- `DeleteDBSubnetGroup` — remove from store
- `DescribeDBSubnetGroups` — list

### Tags (3 ops)
- `AddTagsToResource` — find resource, upsert tags
- `RemoveTagsFromResource` — find resource, remove by key
- `ListTagsForResource` — find resource, return tags

### Engine Versions (1 op)
- `DescribeDBEngineVersions` — return supported Neptune versions

## Phase 2: Deferred (42 ops)
- Event subscriptions (Create/Delete/Modify/Describe)
- Global clusters (Create/Delete/Modify/Describe/Failover/Switchover/RemoveFrom)
- DB cluster endpoints (Create/Delete/Modify/Describe)
- Copy/Restore operations (Copy cluster/param group, Restore from snapshot/PITR)
- Describe variants (OrderableDBInstanceOptions, PendingMaintenanceActions, ValidDBInstanceModifications, Events, EventCategories, EngineDefaultParameters/ClusterParameters)
- Failover operations (FailoverDBCluster, PromoteReadReplicaDBCluster)
- Start/Stop DB cluster
- Modify snapshot attributes
- Add/Remove role/source identifier
- Reset parameter groups to defaults
- Apply pending maintenance actions

## Error Model
All handlers use typed exception classes matching AWS error codes:
- `DBClusterNotFoundFault`, `DBInstanceNotFoundFault`, etc. (404)
- `DBClusterAlreadyExistsFault`, `DBInstanceAlreadyExistsFault`, etc. (409)
- `InvalidParameterValueException`, `InvalidDBClusterStateFault`, etc. (400)
- `DBSubnetGroupDoesNotCoverEnoughAZs`, `SnapshotQuotaExceededFault`, etc. (400)

## Store Design
- `NeptuneStore` — single in-memory store with per-entity dicts
- Case-insensitive key lookups (`.lower()`)
- Store methods raise typed exceptions
- Handlers translate AWS CamelCase request keys to store method parameters

## Testing
- **Integration**: 38 tests across 15 test classes, all passing
- **E2E**: 3 tests written, skipped until provider is wired into localstack
- **Coverage**: Happy path + error path for every Create/Delete operation, Describe verification, tag CRUD
