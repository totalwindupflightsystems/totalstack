---
id: "@specs/aws/dynamodb/batch-get-item"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, batch-get-item]
short: "BatchGetItem operation — retrieve up to 100 items across tables"
---

# BatchGetItem

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc
> **source:** AWS DynamoDB API Reference — BatchGetItem

The `BatchGetItem` operation returns the attributes of one or more items from one or more tables by primary key. A single operation can retrieve up to 16 MB of data, containing up to 100 items. If you request more than 100 items, a `ValidationException` is returned.

If the response size limit is exceeded, throughput is exceeded, more than 1MB per partition is requested, or an internal failure occurs, a partial result is returned with `UnprocessedKeys`. Use this to retry the remaining items with exponential backoff.

If *none* of the items can be processed, `ProvisionedThroughputExceededException` is raised. If at least one item succeeds, the operation completes with `UnprocessedKeys` for the rest. Each table request supports `ConsistentRead`, `ProjectionExpression`, and `ExpressionAttributeNames`.

**Required:** `RequestItems`
**Input shape:** `BatchGetItemInput`
**Output shape:** `BatchGetItemOutput` (Responses, UnprocessedKeys, ConsumedCapacity)

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/batch-get-item
# spec:implements: @kind:operation BatchGetItem

from typing import Dict, Any, List, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def batch_get_item(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    request_items: Dict[str, Dict[str, Any]],
    *,
    return_consumed_capacity: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Retrieve multiple items by primary key across one or more tables.

    @kind:operation BatchGetItem

    Per AWS docs:
    - RequestItems maps table name → {Keys, ProjectionExpression?,
      ExpressionAttributeNames?, ConsistentRead?}
    - Up to 100 keys total across all tables; exceeds → ValidationException.
    - 16 MB response size limit; partial results → UnprocessedKeys.
    - If at least one item succeeds, returns 200 with UnprocessedKeys.
    - If zero items succeed, raises ProvisionedThroughputExceededException.
    - Retry UnprocessedKeys with exponential backoff.
    - ConsistentRead per table (default: eventually consistent).
    - Each table name or ARN can appear only once per request.
    """
    # Validate total key count ≤ 100 (per AWS docs)
    total_keys = 0
    for table_name, request_spec in request_items.items():
        keys = request_spec.get("Keys", [])
        total_keys += len(keys)

    if total_keys > 100:
        raise ValidationException(
            "1 validation error detected: "
            "Too many items requested for the BatchGetItem call."
        )

    responses: Dict[str, List[Dict[str, Any]]] = {}
    unprocessed_keys: Dict[str, Dict[str, Any]] = {}
    consumed_capacity_total: List[Dict[str, Any]] = []
    processed_any = False

    for table_name, request_spec in request_items.items():
        # Resolve table name from ARN if needed
        resolved_table = table_name
        if ":table/" in table_name:
            resolved_table = table_name.split(":table/")[-1]

        # Validate table exists
        table_def = store.table_definitions.get(resolved_table)
        if not table_def:
            raise ResourceNotFoundException(
                f"Requested resource not found: Table: {resolved_table} not found"
            )

        key_schema = table_def["KeySchema"]
        keys = request_spec.get("Keys", [])
        projection = request_spec.get("ProjectionExpression")
        expr_names = request_spec.get("ExpressionAttributeNames")
        consistent_read = request_spec.get("ConsistentRead", False)

        table = store.tables.get(resolved_table, {})
        table_responses: List[Dict[str, Any]] = []
        table_unprocessed: List[Dict[str, Any]] = []

        for key in keys:
            # Validate key has all required key attributes
            valid = True
            for key_elem in key_schema:
                attr_name = key_elem["AttributeName"]
                if attr_name not in key:
                    raise ValidationException(
                        "The provided key element does not match the schema"
                    )

            pk = _key_to_string(key, key_schema)
            item = table.get(pk)

            if item is None:
                # Key not found — still a successful request, just no item
                table_responses.append({})
                processed_any = True
                continue

            # Apply projection if specified
            if projection and item:
                item = _apply_projection(projection, expr_names, item)

            table_responses.append(item)
            processed_any = True

        if table_responses:
            responses[resolved_table] = table_responses

        # Track unprocessed if any (simplified: we process all here,
        # but real implementation would track 16 MB limit breaches)
        if table_unprocessed:
            unprocessed_keys[resolved_table] = {
                "Keys": table_unprocessed,
                "ProjectionExpression": projection,
                "ExpressionAttributeNames": expr_names,
                "ConsistentRead": consistent_read,
            }

        # Consumed capacity per table
        if return_consumed_capacity != "NONE":
            consumed_capacity_total.append({
                "TableName": resolved_table,
                "CapacityUnits": round(len(keys) * 0.5, 2),
            })

    # If zero items processed successfully, per AWS docs raise
    # ProvisionedThroughputExceededException
    if not processed_any:
        raise ProvisionedThroughputExceededException(
            "The level of configured provisioned throughput for the table "
            "was exceeded. Consider increasing your provisioning level with "
            "the UpdateTable API."
        )

    # Build response
    response: Dict[str, Any] = {
        "Responses": responses,
    }

    if unprocessed_keys:
        response["UnprocessedKeys"] = unprocessed_keys

    if return_consumed_capacity != "NONE" and consumed_capacity_total:
        response["ConsumedCapacity"] = consumed_capacity_total

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
    """Apply projection expression to return only specified attributes."""
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


class ProvisionedThroughputExceededException(Exception):
    """Provisioned throughput exceeded."""
    pass
```
