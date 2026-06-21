---
id: "@specs/aws/dynamodb/transact-get-items"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, transact-get-items]
short: "TransactGetItems operation — atomic read of up to 100 items across tables"
---

# TransactGetItems

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc
> **source:** AWS DynamoDB API Reference — TransactGetItems

`TransactGetItems` is a synchronous operation that atomically retrieves multiple items from one or more tables (but not indexes) in a single account and Region. A call can contain up to 100 `TransactGetItem` objects, each with a `Get` structure specifying an item to retrieve. The aggregate size of items in the transaction cannot exceed 4 MB.

DynamoDB rejects the entire request if: a conflicting operation is updating an item to be read, there is insufficient provisioned capacity, there is a user error (e.g., invalid data format), or the aggregate size exceeds 4 MB.

Each `Get` structure contains: `TableName`, `Key` (primary key map), optional `ProjectionExpression`, and optional `ExpressionAttributeNames`. Table names can be provided as ARNs.

**Required:** `TransactItems`
**Input shape:** `TransactGetItemsInput`
**Output shape:** `TransactGetItemsOutput` (Responses, ConsumedCapacity)

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/transact-get-items
# spec:implements: @kind:operation TransactGetItems

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def transact_get_items(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    transact_items: List[Dict[str, Any]],
    *,
    return_consumed_capacity: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Atomically read up to 100 items across one or more tables.

    @kind:operation TransactGetItems

    Per AWS docs:
    - TransactItems is an ordered array of up to 100 TransactGetItem objects.
    - Each entry must have a ``Get`` key with TableName, Key, and optional
      ProjectionExpression/ExpressionAttributeNames.
    - Atomic read across tables with snapshot isolation.
    - Rejects entire request (>4 MB, conflicting writes, insufficient capacity).
    - Cannot retrieve items from indexes — only tables.
    - Returns Responses array (one entry per TransactItem, may be empty for not-found).
    """
    # Validate transact items
    if not transact_items:
        raise ValidationException(
            "1 validation error detected: "
            "Value '[]' at 'transactItems' failed to satisfy constraint: "
            "Member must have length greater than or equal to 1"
        )

    if len(transact_items) > 100:
        raise ValidationException(
            "1 validation error detected: "
            "Value at 'transactItems' failed to satisfy constraint: "
            "Member must have length less than or equal to 100"
        )

    # Snapshot isolation: resolve all gets atomically
    responses: List[Dict[str, Any]] = []
    consumed_capacity_total = 0.0
    tables_touched: Dict[str, float] = {}

    for transact_item in transact_items:
        get_req = transact_item.get("Get")
        if not get_req:
            raise ValidationException(
                "TransactItems must contain a Get key"
            )

        # Resolve table name from ARN if needed
        table_name = get_req.get("TableName", "")
        if not table_name:
            raise ValidationException("TableName is required in Get")

        if ":table/" in table_name:
            table_name = table_name.split(":table/")[-1]

        # Validate table exists
        table_def = store.table_definitions.get(table_name)
        if not table_def:
            raise ResourceNotFoundException(
                f"Requested resource not found: Table: {table_name} not found"
            )

        # Validate key is provided
        key = get_req.get("Key")
        if not key:
            raise ValidationException("Key is required in Get")

        key_schema = table_def.get("KeySchema", [])

        # Validate key has all required key attributes
        for key_elem in key_schema:
            attr_name = key_elem["AttributeName"]
            if attr_name not in key:
                raise ValidationException(
                    "The provided key element does not match the schema"
                )

        pk = _key_to_string(key, key_schema)

        # Look up item
        table = store.tables.get(table_name, {})
        item = table.get(pk)

        # Apply projection expression if provided
        if item is not None and "ProjectionExpression" in get_req:
            item = _apply_projection(
                get_req["ProjectionExpression"],
                get_req.get("ExpressionAttributeNames"),
                item,
            )

        # Build per-item response (empty dict if item not found)
        item_response: Dict[str, Any] = {}
        if item is not None:
            item_response["Item"] = item

        responses.append(item_response)

        # Track consumed capacity
        tables_touched[table_name] = tables_touched.get(table_name, 0) + 0.5
        consumed_capacity_total += 0.5

    # Build response
    response: Dict[str, Any] = {
        "Responses": responses,
    }

    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = [
            {
                "TableName": tn,
                "CapacityUnits": round(cu, 2),
            }
            for tn, cu in sorted(tables_touched.items())
        ]

    return response


def _key_to_string(
    key: Dict[str, Any],
    key_schema: List[Dict[str, str]],
) -> str:
    """Convert a DynamoDB key to a string for hash lookup."""
    parts = []
    for key_elem in key_schema:
        attr_name = key_elem["AttributeName"]
        if attr_name in key:
            value = key[attr_name]
            if "S" in value:
                parts.append(value["S"])
            elif "N" in value:
                parts.append(str(value["N"]))
            elif "B" in value:
                parts.append(value["B"])
    return "|".join(parts)


def _apply_projection(
    projection_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """Apply a projection expression to return only specified attributes."""
    names = expression_attribute_names or {}
    projected: Dict[str, Any] = {}
    parts = [p.strip() for p in projection_expression.split(",")]
    for part in parts:
        resolved = part
        for placeholder, attr_name in names.items():
            resolved = resolved.replace(placeholder, attr_name)
        if resolved in item:
            projected[resolved] = item[resolved]
    return projected


class ResourceNotFoundException(Exception):
    """Table not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass
```
