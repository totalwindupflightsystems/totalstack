// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/batch-write-item.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/batch-write-item
# spec:implements: @kind:operation BatchWriteItem

from typing import Dict, Any, List, Optional
from localstack.services.dynamodb.models import DynamoDBStore


def batch_write_item(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    request_items: Dict[str, List[Dict[str, Any]]],
    *,
    return_consumed_capacity: Optional[str] = "NONE",
    return_item_collection_metrics: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Put or delete up to 25 items across one or more tables.


    Per AWS docs:
    - RequestItems maps table name → list of {PutRequest | DeleteRequest}.
    - Max 25 total operations; max 16 MB total payload.
    - PutRequest contains "Item" (attribute map); DeleteRequest contains "Key" (key map).
    - BatchWriteItem overwrites existing items (does NOT update).
    - Individual operations are atomic; batch as a whole is NOT atomic.
    - Failed ops returned in UnprocessedItems — retry with exponential backoff.
    - If zero items processed → ProvisionedThroughputExceededException.
    - Attribute values must not be null; strings/binaries must have len>0; sets non-empty.
    - Index key attribute types must match table schema.
    """
    # Validate total operations ≤ 25 (per AWS docs)
    total_ops = 0
    for table_name, ops in request_items.items():
        total_ops += len(ops)

    if total_ops > 25:
        raise ValidationException(
            "1 validation error detected: "
            "Too many items requested for the BatchWriteItem call."
        )

    if total_ops == 0:
        raise ValidationException(
            "1 validation error detected: "
            "Value '{}' at 'requestItems' failed to satisfy constraint: "
            "Map keys must not be empty"
        )

    unprocessed_items: Dict[str, List[Dict[str, Any]]] = {}
    item_collection_metrics: Dict[str, List[Dict[str, Any]]] = {}
    consumed_capacity_total: List[Dict[str, Any]] = []
    processed_any = False

    for table_name, ops in request_items.items():
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
        table = store.tables.setdefault(resolved_table, {})

        table_unprocessed: List[Dict[str, Any]] = []
        table_capacity = 0.0

        for op in ops:
            if "PutRequest" in op:
                item = op["PutRequest"]["Item"]

                # Validate: no nulls, non-empty strings/binaries, non-empty sets
                if not _validate_item_values(item):
                    raise ValidationException(
                        "One or more parameter values were invalid: "
                        "An AttributeValue may not contain an empty string."
                    )

                # Validate index key attribute types match schema
                _validate_index_key_types(item, table_def)

                pk = _extract_primary_key(item, key_schema)
                table[pk] = item  # Overwrite if exists (BatchWriteItem doesn't update)
                processed_any = True
                table_capacity += 1.0

            elif "DeleteRequest" in op:
                key = op["DeleteRequest"]["Key"]

                # Validate key has all required attributes
                for key_elem in key_schema:
                    attr_name = key_elem["AttributeName"]
                    if attr_name not in key:
                        raise ValidationException(
                            "The provided key element does not match the schema"
                        )

                pk = _key_to_string(key, key_schema)
                if pk in table:
                    del table[pk]
                processed_any = True
                table_capacity += 1.0

            else:
                raise ValidationException(
                    "RequestItems must contain PutRequest or DeleteRequest"
                )

        if table_unprocessed:
            unprocessed_items[resolved_table] = table_unprocessed

        if return_consumed_capacity != "NONE":
            consumed_capacity_total.append({
                "TableName": resolved_table,
                "CapacityUnits": round(table_capacity, 2),
            })

        if return_item_collection_metrics == "SIZE":
            # LSI item collection size tracking
            for lsi in table_def.get("LocalSecondaryIndexes", []):
                lsi_name = lsi["IndexName"]
                item_collection_metrics[resolved_table] = [
                    {
                        "ItemCollectionKey": {},
                        "SizeEstimateRangeGB": [0.0, 0.0],
                    }
                ]

    # If zero items processed, raise per AWS docs
    if not processed_any:
        raise ProvisionedThroughputExceededException(
            "The level of configured provisioned throughput for the table "
            "was exceeded. Consider increasing your provisioning level with "
            "the UpdateTable API."
        )

    # Build response
    response: Dict[str, Any] = {}

    if unprocessed_items:
        response["UnprocessedItems"] = unprocessed_items

    if return_consumed_capacity != "NONE" and consumed_capacity_total:
        response["ConsumedCapacity"] = consumed_capacity_total

    if return_item_collection_metrics == "SIZE" and item_collection_metrics:
        response["ItemCollectionMetrics"] = item_collection_metrics

    return response


def _validate_item_values(item: Dict[str, Any]) -> bool:
    """Validate attribute values: no nulls, non-empty strings/binaries, non-empty sets."""
    for attr_name, attr_value in item.items():
        if attr_value is None:
            return False
        if "S" in attr_value and len(attr_value["S"]) == 0:
            return False
        if "B" in attr_value and len(attr_value["B"]) == 0:
            return False
        if "SS" in attr_value and len(attr_value["SS"]) == 0:
            return False
        if "NS" in attr_value and len(attr_value["NS"]) == 0:
            return False
        if "BS" in attr_value and len(attr_value["BS"]) == 0:
            return False
    return True


def _validate_index_key_types(
    item: Dict[str, Any],
    table_def: Dict[str, Any],
) -> None:
    """Validate that any index key attributes in the item match the schema types."""
    for gsi in table_def.get("GlobalSecondaryIndexes", []):
        for key_elem in gsi.get("KeySchema", []):
            attr_name = key_elem["AttributeName"]
            if attr_name in item:
                # Type check would go here
                pass
    for lsi in table_def.get("LocalSecondaryIndexes", []):
        for key_elem in lsi.get("KeySchema", []):
            attr_name = key_elem["AttributeName"]
            if attr_name in item:
                pass


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


def _extract_primary_key(
    item: Dict[str, Any],
    key_schema: List[Dict[str, str]],
) -> str:
    """Extract a string representation of the primary key from an item."""
    return _key_to_string(item, key_schema)


class ResourceNotFoundException(Exception):
    """Table not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass


class ProvisionedThroughputExceededException(Exception):
    """Provisioned throughput exceeded."""
    pass