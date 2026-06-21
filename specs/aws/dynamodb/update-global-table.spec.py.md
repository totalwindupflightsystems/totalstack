---
id: "@specs/aws/dynamodb/update-global-table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, update-global-table]
short: "UpdateGlobalTable operation — add or remove replicas from a global table"
---

# UpdateGlobalTable

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Adds or removes replicas in the specified global table. The global table must already exist to be able to use this operation. Any replica to be added must be empty, have the same name as the global table, have the same key schema, have DynamoDB Streams enabled, and have the same provisioned and maximum write capacity units.

> **Note:** This documentation is for version 2017.11.29 (Legacy) of global tables. Customers should use Global Tables version 2019.11.21 (Current) when possible. Although you can use UpdateGlobalTable to add replicas and remove replicas in a single request, for simplicity we recommend that you issue separate requests for adding or removing replicas.

**Required:** `GlobalTableName`, `ReplicaUpdates`
**Input shape:** `UpdateGlobalTableInput`
**Output shape:** `UpdateGlobalTableOutput`

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/update-global-table
# spec:implements: @kind:operation UpdateGlobalTable

from typing import Dict, Any, List, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def update_global_table(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    global_table_name: str,
    replica_updates: List[Dict[str, Optional[Dict[str, str]]]],
) -> Dict[str, Any]:
    """
    Add or remove replicas from a global table.

    @kind:operation UpdateGlobalTable

    replica_updates is a list of update actions, each containing
    either "Create" (add replica) or "Delete" (remove replica):
        [
            {"Create": {"RegionName": "us-west-2"}},
            {"Delete": {"RegionName": "eu-west-1"}},
        ]

    Although both Create and Delete can appear in a single request,
    for simplicity separate requests are recommended per AWS docs.

    Returns GlobalTableDescription with updated ReplicationGroup.
    """
    details = store.GLOBAL_TABLES.get(global_table_name)
    if not details:
        raise GlobalTableNotFoundException(
            "Global table with this name does not exist"
        )

    repl_group: List[Dict[str, str]] = details.get("ReplicationGroup", [])

    for update in replica_updates or []:
        _apply_replica_update(repl_group, update)

    details["ReplicationGroup"] = repl_group
    details["GlobalTableStatus"] = "UPDATING"

    return {"GlobalTableDescription": details}


def _apply_replica_update(
    repl_group: List[Dict[str, str]],
    update: Dict[str, Optional[Dict[str, str]]],
) -> None:
    """Apply a single replica update (Create or Delete)."""
    # Handle Delete: remove replica by RegionName
    delete = update.get("Delete")
    if delete:
        region_to_delete = delete.get("RegionName")
        existing = [
            g for g in repl_group
            if g.get("RegionName") == region_to_delete
        ]
        if not existing:
            raise ReplicaNotFoundException(
                f"Replica not found for region: {region_to_delete}"
            )
        repl_group[:] = [
            g for g in repl_group
            if g.get("RegionName") != region_to_delete
        ]
        return

    # Handle Create: add replica if not already present
    create = update.get("Create")
    if create:
        region_to_create = create.get("RegionName")
        already_exists = any(
            g.get("RegionName") == region_to_create
            for g in repl_group
        )
        if already_exists:
            raise ReplicaAlreadyExistsException(
                f"Replica already exists for region: {region_to_create}"
            )

        new_group: Dict[str, str] = {
            "RegionName": region_to_create,
            "ReplicaStatus": "ACTIVE",
            "ReplicaStatusDescription": "Replica active",
        }
        repl_group.append(new_group)


class GlobalTableNotFoundException(Exception):
    """Global table with this name does not exist."""
    pass


class ReplicaAlreadyExistsException(Exception):
    """Replica already exists in the specified region."""
    pass


class ReplicaNotFoundException(Exception):
    """Replica not found in the specified region."""
    pass
```
