
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/disable-kinesis-streaming-destination
# spec:implements: @kind:operation DisableKinesisStreamingDestination

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def disable_kinesis_streaming_destination(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    stream_arn: str,
    *,
    enable_kinesis_streaming_configuration: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Disable Kinesis Data Streams destination for a DynamoDB table.


    State machine for DestinationStatus:
        ACTIVE → DISABLED (via this operation)

    Output shape (KinesisStreamingDestinationOutput) includes
    EnableKinesisStreamingConfiguration per the API schema even though
    disabling does not change the configuration.

    Validation:
        - Table must exist
        - Kinesis stream must exist
        - The destination must currently be in ACTIVE state
        - If no matching destination exists, raise ValidationException
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Get current streaming destinations for this table
    streaming_destinations: List[Dict[str, Any]] = (
        store.streaming_destinations.get(table_name) or []
    )

    # Find the matching destination
    destinations = [
        d for d in streaming_destinations if d["StreamArn"] == stream_arn
    ]

    if not destinations:
        raise ValidationException(
            "Table is not in a valid state to disable Kinesis Streaming "
            "Destination: DisableKinesisStreamingDestination must be ACTIVE "
            "to perform DISABLE operation."
        )

    # Check that the destination is in a state that can be disabled
    status = destinations[0].get("DestinationStatus")
    if status != "ACTIVE":
        raise ValidationException(
            "Table is not in a valid state to disable Kinesis Streaming "
            f"Destination: DisableKinesisStreamingDestination must be ACTIVE "
            f"to perform DISABLE operation. Current status: {status}"
        )

    # Mark the destination as DISABLED
    destinations[0]["DestinationStatus"] = "DISABLED"
    destinations[0]["DestinationStatusDescription"] = "Stream is disabled"

    # Return output with DISABLING status (eventual consistency per AWS docs)
    # Per KinesisStreamingDestinationOutput shape, include
    # EnableKinesisStreamingConfiguration even though disabling does not
    # modify it
    return {
        "DestinationStatus": "DISABLING",
        "StreamArn": stream_arn,
        "TableName": table_name,
        "EnableKinesisStreamingConfiguration": (
            enable_kinesis_streaming_configuration or {}
        ),
    }


class ResourceNotFoundException(Exception):
    """Table or resource not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass
