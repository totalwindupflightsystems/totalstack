// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/scan.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/scan
# spec:implements: @kind:operation Scan

from typing import Optional, Dict, Any, List, Tuple
from localstack.services.dynamodb.models import DynamoDBStore


def scan(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    table_name: str,
    *,
    index_name: Optional[str] = None,
    filter_expression: Optional[str] = None,
    expression_attribute_names: Optional[Dict[str, str]] = None,
    expression_attribute_values: Optional[Dict[str, Any]] = None,
    projection_expression: Optional[str] = None,
    limit: Optional[int] = None,
    exclusive_start_key: Optional[Dict[str, Any]] = None,
    consistent_read: bool = False,
    select: Optional[str] = None,
    total_segments: Optional[int] = None,
    segment: Optional[int] = None,
    return_consumed_capacity: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Scan all items in a table or index, optionally filtered.


    Per AWS docs:
    - Scans every item in the table/index sequentially; up to 1 MB per request.
    - FilterExpression applied after items are read; filtering costs no extra RCU.
    - ScannedCount = items evaluated; Count = items after filtering.
    - LastEvaluatedKey indicates pagination needed.
    - Parallel scans via Segment (0-based) and TotalSegments (1..1,000,000).
    - ConsistentRead=true not supported on GSIs.
    """
    # Validate table exists
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    # Determine key schema
    if index_name:
        key_schema = _get_index_key_schema(table_def, index_name)
        if not key_schema:
            raise ValidationException(
                f"Requested resource not found: Index: {index_name} for table {table_name}"
            )
        # Consistent read not supported on GSI
        if consistent_read:
            for gsi in table_def.get("GlobalSecondaryIndexes", []):
                if gsi["IndexName"] == index_name:
                    raise ValidationException(
                        "Consistent reads are not supported on global secondary indexes"
                    )
    else:
        key_schema = table_def["KeySchema"]

    # Get all items
    all_items: Dict[str, Dict[str, Any]] = store.tables.get(table_name, {})

    # Convert to list of (pk, item) and sort for deterministic pagination
    items: List[Tuple[str, Dict[str, Any]]] = list(all_items.items())
    items.sort(key=lambda x: _sort_key_for_item(x[1], key_schema))

    # Parallel scan: select items belonging to this segment
    if total_segments is not None and segment is not None:
        # Validate segment range
        if segment < 0 or segment >= total_segments:
            raise ValidationException(
                "Segment must be >= 0 and < TotalSegments"
            )
        items = [
            (pk, item) for i, (pk, item) in enumerate(items)
            if i % total_segments == segment
        ]

    # Apply filter expression (post-scan, no additional RCU)
    if filter_expression:
        items = [
            (pk, item) for pk, item in items
            if _evaluate_filter(
                filter_expression,
                expression_attribute_names,
                expression_attribute_values,
                item,
            )
        ]

    # Handle pagination: ExclusiveStartKey
    start_idx = 0
    if exclusive_start_key:
        start_pk = _key_to_string(exclusive_start_key, key_schema)
        for i, (pk, _) in enumerate(items):
            if pk == start_pk:
                start_idx = i + 1  # Start after the exclusive start key
                break

    # Apply limit
    end_idx = len(items)
    if limit is not None and limit > 0:
        end_idx = min(start_idx + limit, len(items))

    scanned_count = end_idx - start_idx
    page_items = items[start_idx:end_idx]

    # Apply projection
    result_items = [item for _, item in page_items]
    if projection_expression:
        result_items = [
            _apply_projection(projection_expression, expression_attribute_names, item)
            for item in result_items
        ]

    # Handle Select parameter
    if select == "COUNT":
        result_items = []
        count = 0
    else:
        count = len(result_items)

    # Build response
    response: Dict[str, Any] = {
        "Items": result_items,
        "Count": count,
        "ScannedCount": scanned_count,
    }

    # LastEvaluatedKey if more items exist
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
            "CapacityUnits": round(0.5 + (scanned_count * 0.5 / max(len(all_items), 1)), 2),
        }

    return response


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


def _sort_key_for_item(
    item: Dict[str, Any],
    key_schema: List[Dict[str, str]],
) -> str:
    """Build a sort key string from an item's key attributes for ordering."""
    parts = []
    for key_elem in key_schema:
        attr_name = key_elem["AttributeName"]
        if attr_name in item:
            value = item[attr_name]
            if "S" in value:
                parts.append(value["S"])
            elif "N" in value:
                parts.append(value["N"].zfill(20))
            elif "B" in value:
                parts.append(value["B"])
    return "|".join(parts)


def _evaluate_filter(
    filter_expression: str,
    expression_attribute_names: Optional[Dict[str, str]],
    expression_attribute_values: Optional[Dict[str, Any]],
    item: Dict[str, Any],
) -> bool:
    """
    Evaluate a FilterExpression against an item.

    Per AWS docs: FilterExpression cannot reference key attributes.
    Applied after scan reads items; no additional RCU consumed.

    Full expression evaluation in expression-parser.spec.py.md.
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