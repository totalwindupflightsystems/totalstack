---
id: "@specs/aws/dynamodb/enable-kinesis-streaming-destination"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, kinesis, streaming, enable-kinesis-streaming-destination]
short: "EnableKinesisStreamingDestination — start streaming DynamoDB changes to Kinesis"
---

# EnableKinesisStreamingDestination

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Starts table data replication to the specified Kinesis data stream at a timestamp chosen during the enable workflow. If this operation doesn't return results immediately, use DescribeKinesisStreamingDestination to check if streaming to the Kinesis data stream is ACTIVE.

**Required:** `TableName`, `StreamArn`
**Input shape:** `KinesisStreamingDestinationInput`
**Output shape:** `KinesisStreamingDestinationOutput`

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/enable-kinesis-streaming-destination
# spec:implements: @kind:operation EnableKinesisStreamingDestination

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def enable_kinesis_streaming_destination(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    stream_arn: str,
    *,
    enable_kinesis_streaming_configuration: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Enable Kinesis Data Streams destination for a DynamoDB table.

    @kind:operation EnableKinesisStreamingDestination

    enable_kinesis_streaming_configuration (optional):
        {
            "ApproximateCreationDateTimePrecision": "MILLISECOND" | "MICROSECOND"
        }

    State machine for DestinationStatus:
        DISABLED or ENABLE_FAILED → ACTIVE (via this operation)

    Validation:
        - Table must exist
        - Kinesis stream must exist
        - If destination already exists, its status must be DISABLED or
          ENABLE_FAILED (cannot re-enable an already ACTIVE destination)
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Validate kinesis stream exists (delegated to _event_forwarder in provider)
    # In spec form, we assume the stream existence check passes
    enable_kinesis_streaming_configuration = (
        enable_kinesis_streaming_configuration or {}
    )

    # Get current streaming destinations for this table
    streaming_destinations: List[Dict[str, Any]] = (
        store.streaming_destinations.get(table_name) or []
    )

    # Check if this stream is already registered
    existing = [
        d for d in streaming_destinations if d["StreamArn"] == stream_arn
    ]

    if existing:
        status = existing[0].get("DestinationStatus")
        if status not in ("DISABLED", "ENABLE_FAILED", "ENABLED_FAILED", None):
            raise ValidationException(
                "Table is not in a valid state to enable Kinesis Streaming "
                "Destination: EnableKinesisStreamingDestination must be "
                "DISABLED or ENABLE_FAILED to perform ENABLE operation."
            )

    # Remove any existing entry for this stream ARN (idempotent re-enable)
    store.streaming_destinations[table_name] = [
        d for d in streaming_destinations if d["StreamArn"] != stream_arn
    ]

    # Add the newly enabled destination with ACTIVE status
    new_destination: Dict[str, Any] = {
        "DestinationStatus": "ACTIVE",
        "DestinationStatusDescription": "Stream is active",
        "StreamArn": stream_arn,
        "ApproximateCreationDateTimePrecision": (
            enable_kinesis_streaming_configuration.get(
                "ApproximateCreationDateTimePrecision", "MILLISECOND"
            )
        ),
    }
    store.streaming_destinations.setdefault(table_name, []).append(
        new_destination
    )

    # Return output with ENABLING status (eventual consistency per AWS docs)
    return {
        "DestinationStatus": "ENABLING",
        "StreamArn": stream_arn,
        "TableName": table_name,
        "EnableKinesisStreamingConfiguration": (
            enable_kinesis_streaming_configuration
        ),
    }


class ResourceNotFoundException(Exception):
    """Table or resource not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass
```
