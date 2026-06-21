---
id: "@specs/aws/dynamodb/describe-continuous-backups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, describe-continuous-backups, pitr]
short: "DescribeContinuousBackups operation — checks Point-in-Time Recovery status"
---

# DescribeContinuousBackups

> **spec:trace:** specs/aws/dynamodb/enriched-aws-reference.json#DescribeContinuousBackups

Checks the status of continuous backups and point-in-time recovery (PITR) for the specified table. Continuous backups are `ENABLED` on all tables at table creation.

When PITR is enabled, you can restore to any point in time within `EarliestRestorableDateTime` and `LatestRestorableDateTime` (typically 5 minutes before current time). Recovery period: 1–35 days.

Rate limit: 10 calls/sec.

**Required:** `TableName`
**Input shape:** `DescribeContinuousBackupsInput`
**Output shape:** `DescribeContinuousBackupsOutput`
**Output members:** `ContinuousBackupsDescription`
**Errors:** `TableNotFoundException`, `InternalServerError`

## ContinuousBackupsDescription

```json
{
    "ContinuousBackupsStatus": "ENABLED",
    "PointInTimeRecoveryDescription": {
        "PointInTimeRecoveryStatus": "ENABLED" | "DISABLED",
        "EarliestRestorableDateTime": "<timestamp>",
        "LatestRestorableDateTime": "<timestamp>"
    }
}
```

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#DescribeContinuousBackups
# spec:id: @specs/aws/dynamodb/describe-continuous-backups
# spec:implements: @kind:operation DescribeContinuousBackups

from typing import Dict, Any
from localstack.services.dynamodb.models import DynamoDBStore


def describe_continuous_backups(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
) -> Dict[str, Any]:
    """
    Return continuous backups and PITR status for a table.

    @kind:operation DescribeContinuousBackups

    Returns ``{"ContinuousBackupsDescription": {...}}``.
    ContinuousBackupsStatus is always "ENABLED" on all tables.
    """
    # Check if table exists
    if table_name not in store.table_definitions:
        raise TableNotFoundException(f"Table not found: {table_name}")

    # Look for stored continuous backup description
    table_props = store.table_properties.get(table_name, {})
    continuous_backup_description = table_props.get(
        "ContinuousBackupsDescription"
    )

    # Default: Continuous backups ENABLED, PITR DISABLED
    if not continuous_backup_description:
        continuous_backup_description = {
            "ContinuousBackupsStatus": "ENABLED",
            "PointInTimeRecoveryDescription": {
                "PointInTimeRecoveryStatus": "DISABLED",
            },
        }

    return {
        "ContinuousBackupsDescription": continuous_backup_description,
    }


class TableNotFoundException(Exception):
    """Table not found."""
    pass
```

