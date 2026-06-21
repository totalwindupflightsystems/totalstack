---
id: "@specs/aws/dynamodb/update-time-to-live"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, ttl, update-time-to-live]
short: "UpdateTimeToLive operation — enable or disable TTL on a table"
---

# UpdateTimeToLive

> **spec:trace:** specs/aws/dynamodb/enriched-aws-reference.json#UpdateTimeToLive

Enables or disables Time To Live (TTL) for the specified table. When enabled, you must specify an `AttributeName` containing the expiration timestamp in epoch seconds. DynamoDB automatically deletes items whose TTL attribute has passed (best-effort, typically within 2 days of expiration).

**Required:** `TableName`, `TimeToLiveSpecification`
**Input shape:** `UpdateTimeToLiveInput`
**Output shape:** `UpdateTimeToLiveOutput`
**Output members:** `TimeToLiveSpecification`
**Errors:** `ResourceInUseException`, `ResourceNotFoundException`, `LimitExceededException`, `InternalServerError`

## TimeToLiveSpecification

```json
{
    "Enabled": true|false,
    "AttributeName": "string"
}
```

- `Enabled=True` → TTL is activated; `AttributeName` is required
- `Enabled=False` → TTL is disabled; existing specification is retained for audit

## One-Hour Cooldown

After a successful `UpdateTimeToLive` call, it can take up to **one hour** for the change to fully process. Any additional `UpdateTimeToLive` calls for the same table during this one-hour window result in a `ValidationException`.

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/enriched-aws-reference.json#UpdateTimeToLive
# spec:id: @specs/aws/dynamodb/update-time-to-live
# spec:implements: @kind:operation UpdateTimeToLive

from typing import Dict, Any
from datetime import datetime, timedelta
from localstack.services.dynamodb.models import DynamoDBStore


def update_time_to_live(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    time_to_live_specification: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Enable or disable TTL on a table.

    @kind:operation UpdateTimeToLive

    time_to_live_specification shape:
        {
            "Enabled": bool,         # True to enable, False to disable
            "AttributeName": str,    # The attribute name used as TTL timestamp
        }

    When Enabled=True, AttributeName is required and must reference an
    existing attribute. When Enabled=False, TTL is disabled but the
    specification is retained.

    Returns ``{"TimeToLiveSpecification": {...}}``.
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Validate TTL specification
    enabled = time_to_live_specification.get("Enabled", False)
    attribute_name = time_to_live_specification.get("AttributeName")

    if enabled and not attribute_name:
        raise ValidationException(
            "AttributeName is required when enabling TTL"
        )

    # One-hour cooldown: prevent rapid toggles
    current_ttl = store.ttl_specifications.get(table_name)
    if current_ttl and "LastModified" in current_ttl:
        elapsed = datetime.utcnow() - current_ttl["LastModified"]
        if elapsed < timedelta(hours=1):
            raise ValidationException(
                "Time to Live has been modified within the last hour. "
                "Please wait before making another change."
            )

    # Store the TTL specification
    store.ttl_specifications[table_name] = {
        "Enabled": enabled,
        "AttributeName": attribute_name,
        "LastModified": datetime.utcnow(),
    }

    # Return the specification as confirmation
    return {
        "TimeToLiveSpecification": {
            "Enabled": enabled,
            "AttributeName": attribute_name,
        },
    }


class ResourceNotFoundException(Exception):
    """Table or resource not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass
```

