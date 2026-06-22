
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/describe-kinesis-streaming-destination
# spec:implements: @kind:operation DescribeKinesisStreamingDestination

import copy
from typing import Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def describe_kinesis_streaming_destination(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
) -> Dict[str, Any]:
    """
    Return the Kinesis Data Streams destinations for a table.


    Returns KinesisDataStreamDestinations list. Each destination has:
        - StreamArn: The ARN of the Kinesis data stream
        - DestinationStatus: ACTIVE | DISABLED | ENABLING | DISABLING | ENABLE_FAILED
        - DestinationStatusDescription (internal, stripped from response)

    Per AWS API behavior, ApproximateCreationDateTimePrecision and
    DestinationStatusDescription are stripped from the response.
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Get streaming destinations for this table
    table_destinations: List[Dict[str, Any]] = (
        store.streaming_destinations.get(table_name) or []
    )

    # Deep copy and strip internal fields not returned by AWS API
    stream_destinations = copy.deepcopy(table_destinations)
    for destination in stream_destinations:
        destination.pop("ApproximateCreationDateTimePrecision", None)
        destination.pop("DestinationStatusDescription", None)

    return {
        "KinesisDataStreamDestinations": stream_destinations,
        "TableName": table_name,
    }


class ResourceNotFoundException(Exception):
    """Table or resource not found."""
    pass
