---
id: "@specs/aws/dynamodb/update-kinesis-streaming-destination"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, kinesis, streaming, update-kinesis-streaming-destination]
short: "UpdateKinesisStreamingDestination — update Kinesis streaming configuration"
---

# UpdateKinesisStreamingDestination

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

The command to update the Kinesis stream destination. Currently, the only configurable parameter is ApproximateCreationDateTimePrecision (MILLISECOND or MICROSECOND).

**Required:** `TableName`, `StreamArn`
**Input shape:** `UpdateKinesisStreamingDestinationInput`
**Output shape:** `UpdateKinesisStreamingDestinationOutput`

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/update-kinesis-streaming-destination
# spec:implements: @kind:operation UpdateKinesisStreamingDestination

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def update_kinesis_streaming_destination(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    stream_arn: str,
    *,
    update_kinesis_streaming_configuration: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Update an existing Kinesis Data Streams destination configuration.

    @kind:operation UpdateKinesisStreamingDestination

    update_kinesis_streaming_configuration:
        {
            "ApproximateCreationDateTimePrecision": "MILLISECOND" | "MICROSECOND"
        }

    The only configurable field is ApproximateCreationDateTimePrecision,
    which controls the timestamp precision for item-level changes sent
    to the Kinesis stream.

    Validation:
        - Table must exist
        - update_kinesis_streaming_configuration must not be None/empty
        - ApproximateCreationDateTimePrecision must be MILLISECOND or MICROSECOND
        - Destination must exist for the given stream_arn on the table
        - Cannot update to the same precision value already set
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Validate configuration is provided
    if not update_kinesis_streaming_configuration:
        raise ValidationException(
            "Streaming destination cannot be updated with given parameters: "
            "UpdateKinesisStreamingConfiguration cannot be null or contain "
            "only null values"
        )

    # Validate time precision value
    time_precision = update_kinesis_streaming_configuration.get(
        "ApproximateCreationDateTimePrecision"
    )
    if time_precision not in ("MILLISECOND", "MICROSECOND"):
        raise ValidationException(
            f"1 validation error detected: Value '{time_precision}' at "
            "'updateKinesisStreamingConfiguration."
            "approximateCreationDateTimePrecision' "
            "failed to satisfy constraint: Member must satisfy enum value "
            "set: [MILLISECOND, MICROSECOND]"
        )

    # Get current streaming destinations
    table_destinations: List[Dict[str, Any]] = (
        store.streaming_destinations.get(table_name) or []
    )

    # Find the matching destination
    destinations = [
        d for d in table_destinations if d["StreamArn"] == stream_arn
    ]
    if not destinations:
        raise ValidationException(
            "Table is not in a valid state to enable Kinesis Streaming "
            "Destination: No streaming destination with streamArn: "
            f"{stream_arn} found for table with tableName: {table_name}"
        )

    destination = destinations[0]

    # Check that the new precision is different from current
    existing_precision = destination.get("ApproximateCreationDateTimePrecision")
    if existing_precision == time_precision:
        table_id = table_def.get("TableId", "unknown")
        raise ValidationException(
            f"Invalid Request: Precision is already set to the desired "
            f"value of {existing_precision} for tableId: {table_id}, "
            f"kdsArn: {stream_arn}"
        )

    # Update the precision
    destination["ApproximateCreationDateTimePrecision"] = time_precision

    # Also keep the table definition in sync
    kds_destinations = table_def.setdefault(
        "KinesisDataStreamDestinations", []
    )
    for kds_dest in kds_destinations:
        if kds_dest.get("StreamArn") == stream_arn:
            kds_dest["ApproximateCreationDateTimePrecision"] = time_precision

    return {
        "TableName": table_name,
        "StreamArn": stream_arn,
        "DestinationStatus": "UPDATING",
        "UpdateKinesisStreamingConfiguration": {
            "ApproximateCreationDateTimePrecision": time_precision,
        },
    }


class ResourceNotFoundException(Exception):
    """Table or resource not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass
```
