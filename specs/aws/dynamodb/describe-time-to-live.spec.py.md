---
id: "@specs/aws/dynamodb/describe-time-to-live"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, ttl, describe-time-to-live]
short: "DescribeTimeToLive operation — get TTL configuration for a table"
---

# DescribeTimeToLive

> **spec:trace:** specs/aws/dynamodb/enriched-aws-reference.json#DescribeTimeToLive

Returns the current Time To Live (TTL) configuration for the specified table. TTL lets you define a per-item timestamp attribute (epoch seconds) that DynamoDB uses to automatically delete expired items.

**Required:** `TableName`
**Input shape:** `DescribeTimeToLiveInput`
**Output shape:** `DescribeTimeToLiveOutput`
**Output members:** `TimeToLiveDescription`
**Errors:** `ResourceNotFoundException`, `InternalServerError`

## TimeToLiveDescription

- `TimeToLiveStatus`: `"ENABLED"` or `"DISABLED"`
- `AttributeName`: name of the timestamp attribute (only present when ENABLED)

If TTL has never been configured or was disabled, returns status `DISABLED` with no `AttributeName`.

## Implementation

```speclang
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

    @kind:operation DescribeTimeToLive

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
```

