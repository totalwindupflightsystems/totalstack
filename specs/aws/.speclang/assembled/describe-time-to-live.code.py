// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/describe-time-to-live.spec.py.md#timetolivedescription
// spec:generated DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#DescribeTimeToLive
# spec:id: @specs/aws/dynamodb/describe-time-to-live
# spec:implements: @kind:operation DescribeTimeToLive

from typing import Dict, Any
from localstack.services.dynamodb.models import DynamoDBStore


def describe_time_to_live(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
) -> Dict[str, Any]:
    """
    Return the current TTL configuration for a table.


    TTL specifications are stored in ``store.ttl_specifications`` keyed
    by table name. Each spec has: Enabled (bool), AttributeName (str,
    the timestamp attribute).

    Returns ``{"TimeToLiveDescription": {...}}``.
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Look up TTL specification
    ttl_spec = store.ttl_specifications.get(table_name)

    # Default: DISABLED with no attribute
    if ttl_spec and ttl_spec.get("Enabled", False):
        time_to_live_description: Dict[str, Any] = {
            "TimeToLiveStatus": "ENABLED",
            "AttributeName": ttl_spec.get("AttributeName"),
        }
    else:
        time_to_live_description = {
            "TimeToLiveStatus": "DISABLED",
        }

    return {
        "TimeToLiveDescription": time_to_live_description,
    }


class ResourceNotFoundException(Exception):
    """Table or resource not found."""
    pass