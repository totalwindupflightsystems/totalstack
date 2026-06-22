
{
    "PointInTimeRecoveryEnabled": true | false
}

## Implementation

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
