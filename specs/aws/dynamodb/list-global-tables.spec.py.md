---
id: "@specs/aws/dynamodb/list-global-tables"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, list-global-tables]
short: "ListGlobalTables operation — lists all global tables (paginated)"
---

# ListGlobalTables

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Lists all global tables that have a replica in the specified Region. Supports pagination via ExclusiveStartGlobalTableName and Limit. If the number of global tables reaches the limit, the operation stops and returns the table names collected up to that point, with a table name in LastEvaluatedGlobalTableName to apply in a subsequent operation to the ExclusiveStartGlobalTableName parameter.

> **Note:** This documentation is for version 2017.11.29 (Legacy) of global tables. Customers should use Global Tables version 2019.11.21 (Current) when possible.

**Required:** none
**Input shape:** `ListGlobalTablesInput`
**Output shape:** `ListGlobalTablesOutput`

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/list-global-tables
# spec:implements: @kind:operation ListGlobalTables

from typing import Dict, Any, List, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def _select_attributes(
    obj: Dict[str, Any],
    attrs: List[str],
) -> Dict[str, Any]:
    """Return a dict with only the requested attributes."""
    return {k: v for k, v in obj.items() if k in attrs}


def list_global_tables(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    *,
    exclusive_start_global_table_name: Optional[str] = None,
    limit: Optional[int] = None,
    region_name_filter: Optional[str] = None,
) -> Dict[str, Any]:
    """
    List all global tables, with optional pagination.

    @kind:operation ListGlobalTables

    Optional parameters:
        - exclusive_start_global_table_name: the first global table name
          that this operation will evaluate (for pagination)
        - limit: maximum number of table names to return (default 100)
        - region_name_filter: lists the global tables in a specific Region

    Returns GlobalTables list (each with GlobalTableName and ReplicationGroup)
    and LastEvaluatedGlobalTableName if more results exist.
    """
    # Collect all global tables
    all_global_tables: List[Dict[str, Any]] = [
        _select_attributes(tab, ["GlobalTableName", "ReplicationGroup"])
        for tab in store.GLOBAL_TABLES.values()
    ]

    # Filter by region if specified
    if region_name_filter:
        all_global_tables = [
            t for t in all_global_tables
            if any(
                r.get("RegionName") == region_name_filter
                for r in t.get("ReplicationGroup", [])
            )
        ]

    # Sort by GlobalTableName for deterministic pagination
    all_global_tables.sort(key=lambda t: t.get("GlobalTableName", ""))

    # Apply ExclusiveStartGlobalTableName pagination
    start_idx = 0
    if exclusive_start_global_table_name:
        for i, gt in enumerate(all_global_tables):
            if gt.get("GlobalTableName") == exclusive_start_global_table_name:
                start_idx = i + 1
                break

    # Apply limit (default 100 per AWS docs)
    effective_limit = limit if limit is not None and limit > 0 else 100
    page = all_global_tables[start_idx : start_idx + effective_limit]

    response: Dict[str, Any] = {"GlobalTables": page}

    # LastEvaluatedGlobalTableName if more items exist
    if (start_idx + effective_limit) < len(all_global_tables):
        last = all_global_tables[start_idx + effective_limit - 1]
        response["LastEvaluatedGlobalTableName"] = last.get("GlobalTableName")

    return response
```
