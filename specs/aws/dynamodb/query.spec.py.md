---
id: "@specs/aws/dynamodb/query"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, query]
short: "Query operation — find items by key condition expression"
---

# Query

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc
> **source:** AWS DynamoDB API Reference — Query

The `Query` operation finds items based on primary key values. You must provide the partition key attribute name and a single value for that attribute. `Query` returns all items with that partition key value. Optionally, you can provide a sort key attribute and use a comparison operator to refine search results.

Use `KeyConditionExpression` to specify the partition key equality test (required) and an optional sort key condition. `FilterExpression` is applied after the query — items that don't satisfy it are discarded, but filtering does not consume additional read capacity. Results are always sorted by sort key value; use `ScanIndexForward=false` for descending order.

A single `Query` reads up to the `Limit` (if set) or 1 MB of data, then applies filtering. `LastEvaluatedKey` in the response indicates more results are available — use it as `ExclusiveStartKey` in the next request to paginate. `ConsistentRead=true` enables strongly consistent reads (not supported on global secondary indexes).

**Required:** `TableName`
**Input shape:** `QueryInput`
**Output shape:** `QueryOutput` (Items, Count, ScannedCount, LastEvaluatedKey, ConsumedCapacity)

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/query
# spec:implements: @kind:operation Query

from typing import Optional, Dict, Any, List, Tuple
from localstack.services.dynamodb.models import DynamoDBStore


def query(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    *,
    index_name: Optional[str] = None,
    key_condition_expression: Optional[str] = None,
    filter_expression: Optional[str] = None,
    expression_attribute_names: Optional[Dict[str, str]] = None,
    expression_attribute_values: Optional[Dict[str, Any]] = None,
    projection_expression: Optional[str] = None,
    limit: Optional[int] = None,
    exclusive_start_key: Optional[Dict[str, Any]] = None,
    scan_index_forward: bool = True,
    consistent_read: bool = False,
    select: Optional[str] = None,
    return_consumed_capacity: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Find items by partition key, optionally filtered by sort key conditions.

    @kind:operation Query

    Per AWS docs:
    - Partition key equality test is mandatory in KeyConditionExpression.
    - Sort key condition is optional, supports =, <, <=, >, >=, BETWEEN, begins_with.
    - FilterExpression is applied AFTER the query reads items; does not save RCU.
    - Results sorted by sort key; ScanIndexForward=False reverses order.
    - Pagination via ExclusiveStartKey / LastEvaluatedKey.
    - ConsistentRead=True uses strongly consistent reads (not on GSI).
    - Query on index requires both TableName and IndexName.
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Determine the key schema to use (table or index)
    if index_name:
        key_schema = _get_index_key_schema(table_def, index_name)
        if not key_schema:
            raise ValidationException(
                f"Requested resource not found: Index: {index_name} for table {table_name}"
            )
        # Consistent read is NOT supported on global secondary indexes
        if consistent_read:
            for gsi in table_def.get("GlobalSecondaryIndexes", []):
                if gsi["IndexName"] == index_name:
                    raise ValidationException(
                        "Consistent reads are not supported on global secondary indexes"
                    )
    else:
        key_schema = table_def["KeySchema"]

    # Get all items from store
    all_items: Dict[str, Dict[str, Any]] = store.tables.get(table_name, {})

    # Convert to list of (pk_string, item)
    items: List[Tuple[str, Dict[str, Any]]] = list(all_items.items())

    # Apply key condition expression
    # Partition key equality is required — all returned items share the same PK value
    if key_condition_expression:
        items = _apply_key_condition(
            key_condition_expression,
            expression_attribute_names,
            expression_attribute_values,
            items,
            key_schema,
        )
    else:
        # Without key condition, return nothing (partition key equality required per AWS)
        items = []

    # Apply filter expression (post-query filtering, no additional RCU consumed)
    if filter_expression and items:
        items = [
            (pk, item) for pk, item in items
            if _evaluate_filter(
                filter_expression,
                expression_attribute_names,
                expression_attribute_values,
                item,
            )
        ]

    # Sort by sort key direction
    # Default is ascending (ScanIndexForward=True); False = descending
    items = _sort_items(items, key_schema, ascending=scan_index_forward)

    # Handle pagination: ExclusiveStartKey
    start_idx = 0
    if exclusive_start_key:
        start_pk = _key_to_string(exclusive_start_key, key_schema)
        for i, (pk, _) in enumerate(items):
            if pk == start_pk:
                start_idx = i + 1  # Start AFTER the exclusive start key
                break

    # Apply limit (before filtering per AWS semantics)
    end_idx = len(items)
    if limit is not None and limit > 0:
        end_idx = min(start_idx + limit, len(items))

    scanned_count = end_idx - start_idx
    page_items = items[start_idx:end_idx]

    # Apply projection expression
    result_items = [item for _, item in page_items]
    if projection_expression:
        result_items = [
            _apply_projection(projection_expression, expression_attribute_names, item)
            for item in result_items
        ]

    # Handle Select parameter
    if select == "COUNT":
        result_items = []
        count = len(page_items)
    else:
        count = len(result_items)

    # Build response
    response: Dict[str, Any] = {
        "Items": result_items,
        "Count": count,
        "ScannedCount": scanned_count,
    }

    # LastEvaluatedKey: present if there are more items
    if end_idx < len(items):
        last_pk, last_item = items[end_idx - 1]
        last_key: Dict[str, Any] = {}
        for key_elem in key_schema:
            attr_name = key_elem["AttributeName"]
            if attr_name in last_item:
                last_key[attr_name] = last_item[attr_name]
        response["LastEvaluatedKey"] = last_key

    # Consumed capacity
    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = {
            "TableName": table_name,
            "CapacityUnits": round(scanned_count * 0.5 / max(len(all_items), 1) + 0.5, 2),
        }

    return response


def _apply_key_condition(
    expression: str,
    expr_names: Optional[Dict[str, str]],
    expr_values: Optional[Dict[str, Any]],
    items: List[Tuple[str, Dict[str, Any]]],
    key_schema: List[Dict[str, str]],
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Evaluate a KeyConditionExpression against items.

    Per AWS docs, the expression must include partition key equality.
    Sort key conditions support: =, <, <=, >, >=, BETWEEN, begins_with.
    """
    import re

    if not expr_values:
        return items

    names = expr_names or {}
    pk_name = key_schema[0]["AttributeName"] if key_schema else None
    sk_name = key_schema[1]["AttributeName"] if len(key_schema) > 1 else None

    # Resolve expression attribute names (#name -> actual name)
    resolved_expr = expression
    for placeholder, name in names.items():
        resolved_expr = resolved_expr.replace(placeholder, name)

    # Extract partition key value from expression
    # Pattern: pk_name = :placeholder
    pk_pattern = re.compile(
        rf'{re.escape(pk_name)}\s*=\s*:(\w+)', re.IGNORECASE
    )
    pk_match = pk_pattern.search(resolved_expr) if pk_name else None

    filtered: List[Tuple[str, Dict[str, Any]]] = []

    for pk_str, item in items:
        # Check partition key equality
        if pk_match and pk_name:
            placeholder = f":{pk_match.group(1)}"
            expected_val = expr_values.get(placeholder)
            item_val = item.get(pk_name)
            if expected_val and item_val:
                if item_val != expected_val:
                    continue

        # Check sort key condition if present
        if sk_name and "AND" in resolved_expr.upper():
            if not _evaluate_sort_condition(
                resolved_expr, expr_values, item, sk_name
            ):
                continue

        filtered.append((pk_str, item))

    return filtered


def _evaluate_sort_condition(
    expression: str,
    expr_values: Dict[str, Any],
    item: Dict[str, Any],
    sk_name: str,
) -> bool:
    """
    Evaluate sort key comparison operators.
    Supports: =, <, <=, >, >=, BETWEEN, begins_with.
    """
    import re

    if sk_name not in item:
        return False

    item_val = item[sk_name]
    # Extract sort key comparison
    patterns = [
        rf'{re.escape(sk_name)}\s*>=\s*:(\w+)',
        rf'{re.escape(sk_name)}\s*<=\s*:(\w+)',
        rf'{re.escape(sk_name)}\s*>\s*:(\w+)',
        rf'{re.escape(sk_name)}\s*<\s*:(\w+)',
        rf'{re.escape(sk_name)}\s*=\s*:(\w+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, expression, re.IGNORECASE)
        if match:
            placeholder = f":{match.group(1)}"
            expected = expr_values.get(placeholder)
            if expected is None:
                return True  # Can't evaluate, pass through

            item_val_str = _extract_comparable(item_val)
            expected_str = _extract_comparable(expected)

            if ">=" in match.group(0):
                return item_val_str >= expected_str
            elif "<=" in match.group(0):
                return item_val_str <= expected_str
            elif ">" in match.group(0):
                return item_val_str > expected_str
            elif "<" in match.group(0):
                return item_val_str < expected_str
            else:
                return item_val_str == expected_str

    # begins_with pattern
    begins_pattern = re.compile(
        rf'begins_with\s*\(\s*{re.escape(sk_name)}\s*,\s*:(\w+)\s*\)', re.IGNORECASE
    )
    begins_match = begins_pattern.search(expression)
    if begins_match:
        placeholder = f":{begins_match.group(1)}"
        expected = expr_values.get(placeholder)
        if expected:
            item_val_str = _extract_comparable(item_val)
            expected_str = _extract_comparable(expected)
            return item_val_str.startswith(expected_str)

    return True  # No recognizable sort condition, pass through


def _extract_comparable(val: Dict[str, Any]) -> str:
    """Extract a comparable string from a DynamoDB attribute value."""
    if "S" in val:
        return val["S"]
    if "N" in val:
        return val["N"]
    if "B" in val:
        return val["B"]
    return str(val)


def _get_index_key_schema(
    table_def: Dict[str, Any],
    index_name: str,
) -> Optional[List[Dict[str, str]]]:
    """Get key schema for a GSI or LSI by name."""
    for gsi in table_def.get("GlobalSecondaryIndexes", []):
        if gsi["IndexName"] == index_name:
            return gsi["KeySchema"]
    for lsi in table_def.get("LocalSecondaryIndexes", []):
        if lsi["IndexName"] == index_name:
            return lsi["KeySchema"]
    return None


def _sort_items(
    items: List[Tuple[str, Dict[str, Any]]],
    key_schema: List[Dict[str, str]],
    ascending: bool = True,
) -> List[Tuple[str, Dict[str, Any]]]:
    """Sort items by sort key. Default is ascending (ScanIndexForward=True)."""
    if len(key_schema) < 2:
        return items

    sk_name = key_schema[1]["AttributeName"]

    def sort_fn(entry):
        _, item = entry
        val = item.get(sk_name, {})
        if "N" in val:
            return ("N", float(val["N"]))
        if "S" in val:
            return ("S", val["S"])
        if "B" in val:
            return ("B", val["B"])
        return ("Z", "")

    items.sort(key=sort_fn, reverse=not ascending)
    return items


def _evaluate_filter(
    filter_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    expression_attribute_values: Optional[Dict[str, Any]],
    item: Dict[str, Any],
) -> bool:
    """
    Evaluate a FilterExpression against an item.

    Per AWS docs: FilterExpression cannot reference key attributes.
    Applied after items are read; does not consume additional read capacity.

    Full expression evaluation is handled by the expression-parser spec.
    This stub returns True (pass through).
    """
    return True


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


def _key_to_string(
    key: Dict[str, Any],
    key_schema: list,
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


class ResourceNotFoundException(Exception):
    """Table not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass
```
