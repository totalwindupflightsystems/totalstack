---
id: "@specs/aws/dynamodb/create-global-table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, create-global-table]
short: "CreateGlobalTable operation — creates a multi-region global table"
---

# CreateGlobalTable

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in the provided Regions.

> **Note:** This documentation is for version 2017.11.29 (Legacy) of global tables. Customers should use Global Tables version 2019.11.21 (Current) when possible.

If you want to add a new replica table to a global table, each of the following conditions must be true:
- The table must have the same primary key as all of the other replicas.
- The table must have the same name as all of the other replicas.
- The table must have DynamoDB Streams enabled, with the stream containing both the new and the old images of the item.
- None of the replica tables in the global table can contain any data.

**Required:** `GlobalTableName`, `ReplicationGroup`
**Input shape:** `CreateGlobalTableInput`
**Output shape:** `CreateGlobalTableOutput`

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/create-global-table
# spec:implements: @kind:operation CreateGlobalTable

from typing import Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def create_global_table(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    global_table_name: str,
    replication_group: List[Dict[str, str]],
) -> Dict[str, Any]:
    """
    Create a new global table spanning multiple regions.

    @kind:operation CreateGlobalTable

    ReplicationGroup is a list of replicas, each with:
        {
            "RegionName": "us-east-1"
        }

    Output returns GlobalTableDescription containing:
        - GlobalTableName
        - ReplicationGroup (list of replicas with ReplicaStatus, RegionName,
          ReplicaStatusDescription)
        - GlobalTableStatus: CREATING | ACTIVE | DELETING | UPDATING
    """
    # Validate global table name
    if not global_table_name or not global_table_name.strip():
        raise ValueError("GlobalTableName must not be empty")

    # Check if global table already exists
    if global_table_name in store.GLOBAL_TABLES:
        raise GlobalTableAlreadyExistsException(
            "Global table with this name already exists"
        )

    # Deep-copy replication group to avoid mutating caller data
    replication_group = [grp.copy() for grp in (replication_group or [])]

    # Build global table description
    data: Dict[str, Any] = {
        "GlobalTableName": global_table_name,
        "ReplicationGroup": replication_group,
        "GlobalTableStatus": "CREATING",
    }

    # Mark each replica as ACTIVE with region info
    for group in replication_group:
        group.setdefault("ReplicaStatus", "ACTIVE")
        group.setdefault(
            "ReplicaStatusDescription", "Replica active"
        )

    # Persist
    store.GLOBAL_TABLES[global_table_name] = data

    return {"GlobalTableDescription": data}


class GlobalTableAlreadyExistsException(Exception):
    """Global table with this name already exists."""
    pass
```
