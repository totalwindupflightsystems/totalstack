
{
    "ContinuousBackupsStatus": "ENABLED",
    "PointInTimeRecoveryDescription": {
        "PointInTimeRecoveryStatus": "ENABLED" | "DISABLED",
        "EarliestRestorableDateTime": "<timestamp>",
        "LatestRestorableDateTime": "<timestamp>"
    }
}

## Implementation

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
