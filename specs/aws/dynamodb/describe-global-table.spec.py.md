---
id: "@specs/aws/dynamodb/describe-global-table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, describe-global-table]
short: "DescribeGlobalTable operation — returns metadata about a global table"
---

# DescribeGlobalTable

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Returns information about the specified global table.

> **Note:** This documentation is for version 2017.11.29 (Legacy) of global tables. Customers should use Global Tables version 2019.11.21 (Current) when possible.

**Required:** `GlobalTableName`
**Input shape:** `DescribeGlobalTableInput`
**Output shape:** `DescribeGlobalTableOutput`

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/describe-global-table
# spec:implements: @kind:operation DescribeGlobalTable

from typing import Dict, Any
from localstack.services.dynamodb.models import DynamoDBStore


def describe_global_table(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    global_table_name: str,
) -> Dict[str, Any]:
    """
    Return metadata about a global table.

    @kind:operation DescribeGlobalTable

    Returns GlobalTableDescription with:
        - GlobalTableName
        - ReplicationGroup (list of replicas with RegionName, ReplicaStatus,
          ReplicaStatusDescription)
        - GlobalTableStatus: CREATING | ACTIVE | DELETING | UPDATING
    """
    details = store.GLOBAL_TABLES.get(global_table_name)
    if not details:
        raise GlobalTableNotFoundException(
            "Global table with this name does not exist"
        )

    return {"GlobalTableDescription": details}


class GlobalTableNotFoundException(Exception):
    """Global table with this name does not exist."""
    pass
```
