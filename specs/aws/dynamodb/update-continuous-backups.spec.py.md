---
id: "@specs/aws/dynamodb/update-continuous-backups"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, update-continuous-backups, pitr]
short: "UpdateContinuousBackups operation — enables or disables Point-in-Time Recovery"
---

# UpdateContinuousBackups

> **spec:trace:** specs/aws/dynamodb/enriched-aws-reference.json#UpdateContinuousBackups

Enables or disables point-in-time recovery (PITR) for the specified table. A successful call returns the current `ContinuousBackupsDescription`. Continuous backups are `ENABLED` on all tables at creation and cannot be disabled.

When PITR is enabled, you can restore to any point in time within `EarliestRestorableDateTime` and `LatestRestorableDateTime` (typically 5 minutes before current time). Recovery period: 1–35 days.

**Required:** `TableName`, `PointInTimeRecoverySpecification`
**Input shape:** `UpdateContinuousBackupsInput`
**Output shape:** `UpdateContinuousBackupsOutput`
**Output members:** `ContinuousBackupsDescription`
**Errors:** `TableNotFoundException`, `ContinuousBackupsUnavailableException`, `InternalServerError`

## PointInTimeRecoverySpecification

```json
{
    "PointInTimeRecoveryEnabled": true | false
}
```

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#UpdateContinuousBackups
# spec:id: @specs/aws/dynamodb/update-continuous-backups
# spec:implements: @kind:operation UpdateContinuousBackups

from typing import Dict, Any
from localstack.services.dynamodb.models import DynamoDBStore


def update_continuous_backups(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    point_in_time_recovery_specification: Dict[str, bool],
) -> Dict[str, Any]:
    """
    Enable or disable Point-in-Time Recovery for a table.

    @kind:operation UpdateContinuousBackups

    point_in_time_recovery_specification format:
        {"PointInTimeRecoveryEnabled": True | False}

    ContinuousBackupsStatus is always "ENABLED" and cannot be changed.
    Only PointInTimeRecoveryStatus is toggled.

    Returns ``{"ContinuousBackupsDescription": {...}}``.
    """
    # Check if table exists
    if table_name not in store.table_definitions:
        raise TableNotFoundException(f"Table not found: {table_name}")

    # Determine PITR status from input
    pitr_enabled = point_in_time_recovery_specification.get(
        "PointInTimeRecoveryEnabled", False
    )
    pitr_status = "ENABLED" if pitr_enabled else "DISABLED"

    # Build continuous backups description
    continuous_backup_description: Dict[str, Any] = {
        "ContinuousBackupsStatus": "ENABLED",
        "PointInTimeRecoveryDescription": {
            "PointInTimeRecoveryStatus": pitr_status,
        },
    }

    # Persist in table_properties
    table_props = store.table_properties.setdefault(table_name, {})
    table_props["ContinuousBackupsDescription"] = continuous_backup_description

    return {
        "ContinuousBackupsDescription": continuous_backup_description,
    }


class TableNotFoundException(Exception):
    """Table not found."""
    pass
```

