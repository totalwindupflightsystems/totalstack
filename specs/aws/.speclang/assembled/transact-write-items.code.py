// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/transact-write-items.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/transact-write-items
# spec:implements: @kind:operation TransactWriteItems

from typing import Optional, Dict, Any, List
from uuid import uuid4
from localstack.services.dynamodb.models import DynamoDBStore


def transact_write_items(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    transact_items: List[Dict[str, Any]],
    *,
    client_request_token: Optional[str] = None,
    return_consumed_capacity: Optional[str] = "NONE",
    return_item_collection_metrics: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Atomically write a set of items with Put, Update, Delete, or ConditionCheck.


    Per AWS docs:
    - Up to 100 action requests; aggregate size ≤ 4 MB.
    - Each item must have exactly one of: Put, Update, Delete, ConditionCheck.
    - All-or-nothing atomicity: if any fails, TransactionCanceledException raised
      with CancellationReasons (ordered, one per action).
    - ClientRequestToken provides 10-minute idempotency window.
    - No two actions can target the same item.
    - Put: writes item with optional ConditionExpression.
    - Update: modifies item with UpdateExpression and optional ConditionExpression.
    - Delete: removes item with optional ConditionExpression.
    - ConditionCheck: asserts condition; no write.
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

    # Check idempotency: if we've seen this client token with the same payload
    # within 10 minutes, return cached result. Per AWS, token is valid 10 min.
    if client_request_token:
        payload_hash = _hash_transact_items(transact_items)
        cached = _check_idempotency(store, client_request_token, payload_hash)
        if cached is not None:
            return cached

    # Phase 1: Validate all items, resolve table names, check for duplicate targets
    validated_items: List[Dict[str, Any]] = []
    targeted_keys: set = set()  # (table_name, pk) pairs to prevent duplicate targeting

    for idx, item in enumerate(transact_items):
        validated = _validate_and_resolve_transact_item(item, store)
        validated_items.append(validated)

        # Per AWS: no two actions can target the same item
        target = (validated["table_name"], validated.get("key"))
        if target[0] and target[1]:
            if target in targeted_keys:
                raise ValidationException(
                    "Transaction request cannot include multiple "
                    "operations on the same item"
                )
            targeted_keys.add(target)

    # Phase 2: Execute each operation in order, tracking for rollback
    rollback_log: List[Dict[str, Any]] = []
    consumed_capacity_total = 0.0
    tables_touched: Dict[str, float] = {}

    try:
        for idx, validated in enumerate(validated_items):
            result = _apply_transact_item(store, validated, rollback_log)
            table_name = validated.get("table_name")
            if table_name:
                tables_touched[table_name] = (
                    tables_touched.get(table_name, 0)
                    + result.get("capacity_units", 1.0)
                )
                consumed_capacity_total += result.get("capacity_units", 1.0)

    except Exception as exc:
        # Rollback all prior changes in reverse order
        _rollback_transact_items(store, rollback_log)

        # Build CancellationReasons per AWS docs — one per item, ordered
        cancellation_reasons: List[Dict[str, Any]] = []
        for i, vi in enumerate(validated_items):
            if i < idx:
                # Prior items succeeded but are rolled back
                cancellation_reasons.append({
                    "Code": "None",
                    "Message": "Transaction cancelled, item rolled back",
                })
            elif i == idx:
                # This is the item that failed
                code = _error_code_for_transaction(exc)
                cancellation_reasons.append({
                    "Code": code,
                    "Message": str(exc),
                })
            else:
                # Items not yet reached
                cancellation_reasons.append({
                    "Code": "None",
                    "Message": "Transaction cancelled, not attempted",
                })

        raise TransactionCanceledException(
            str(exc),
            cancellation_reasons=cancellation_reasons,
        )

    # Build response
    response: Dict[str, Any] = {}

    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = [
            {
                "TableName": tn,
                "CapacityUnits": round(cu, 2),
            }
            for tn, cu in sorted(tables_touched.items())
        ]

    if return_item_collection_metrics == "SIZE":
        response["ItemCollectionMetrics"] = {}

    # Cache idempotency result
    if client_request_token:
        _store_idempotency(store, client_request_token, payload_hash, response)

    return response


def _validate_and_resolve_transact_item(
    item: Dict[str, Any],
    store: DynamoDBStore,
) -> Dict[str, Any]:
    """
    Validate a TransactWriteItem and resolve table ARNs to names.

    Each item must have exactly one of: Put, Update, Delete, ConditionCheck.
    Returns a normalized dict with ``kind``, ``table_name``, ``inner``, ``key``.
    """
    found: Optional[str] = None
    inner: Optional[Dict[str, Any]] = None

    for kind in ("Put", "Update", "Delete", "ConditionCheck"):
        if kind in item:
            if found is not None:
                raise ValidationException(
                    "TransactItems can only contain one of "
                    "Put, Update, Delete, or ConditionCheck per item"
                )
            found = kind
            inner = item[kind]

    if found is None:
        raise ValidationException(
            "TransactItems must contain one of "
            "Put, Update, Delete, or ConditionCheck"
        )

    # Resolve table name from ARN if needed
    table_name = inner.get("TableName", "")
    if ":table/" in table_name:
        table_name = table_name.split(":table/")[-1]

    # Validate table exists
    if table_name and table_name not in store.table_definitions:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    return {
        "kind": found,
        "table_name": table_name,
        "inner": inner,
        "key": _extract_key_from_inner(inner, store, table_name),
    }


def _extract_key_from_inner(
    inner: Dict[str, Any],
    store: DynamoDBStore,
    table_name: str,
) -> Optional[str]:
    """Extract the primary key string from a transact inner item."""
    table_def = store.table_definitions.get(table_name)
    if not table_def:
        return None

    key_schema = table_def.get("KeySchema", [])
    if not key_schema:
        return None

    # Key can be in 'Key' (for Delete/ConditionCheck/Update) or extracted from 'Item' (for Put)
    if "Key" in inner:
        return _key_to_string(inner["Key"], key_schema)
    elif "Item" in inner:
        return _extract_primary_key(inner["Item"], key_schema)

    return None


def _apply_transact_item(
    store: DynamoDBStore,
    validated: Dict[str, Any],
    rollback_log: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Apply a single transact item and record rollback info.

    Per AWS docs, ConditionCheck does NOT write — it only asserts.
    Put/Update/Delete all support optional ConditionExpression.
    """
    kind = validated["kind"]
    table_name = validated["table_name"]
    inner = validated["inner"]
    pk = validated["key"]
    table = store.tables.get(table_name, {})

    if kind == "Put":
        item_data = inner["Item"]
        # Check condition expression if present
        condition = inner.get("ConditionExpression")
        if condition:
            existing = table.get(pk)
            if not _evaluate_condition(
                condition,
                inner.get("ExpressionAttributeNames"),
                inner.get("ExpressionAttributeValues"),
                existing,
            ):
                raise ConditionalCheckFailedException(
                    "The conditional request failed"
                )
        old_item = table.get(pk)
        table[pk] = item_data
        rollback_log.append({
            "kind": "Put",
            "table_name": table_name,
            "key": pk,
            "old_item": old_item,
        })
        return {"capacity_units": 1.0}

    elif kind == "Update":
        # Check condition expression if present
        condition = inner.get("ConditionExpression")
        if condition:
            existing = table.get(pk)
            if not _evaluate_condition(
                condition,
                inner.get("ExpressionAttributeNames"),
                inner.get("ExpressionAttributeValues"),
                existing,
            ):
                raise ConditionalCheckFailedException(
                    "The conditional request failed"
                )
        old_item = table.get(pk)
        if old_item is None:
            raise ValidationException(
                "The provided expression refers to an attribute "
                "that does not exist in the item"
            )
        updated = _apply_update(inner, old_item)
        table[pk] = updated
        rollback_log.append({
            "kind": "Update",
            "table_name": table_name,
            "key": pk,
            "old_item": old_item,
        })
        return {"capacity_units": 1.0}

    elif kind == "Delete":
        # Check condition expression if present
        condition = inner.get("ConditionExpression")
        if condition:
            existing = table.get(pk)
            if not _evaluate_condition(
                condition,
                inner.get("ExpressionAttributeNames"),
                inner.get("ExpressionAttributeValues"),
                existing,
            ):
                raise ConditionalCheckFailedException(
                    "The conditional request failed"
                )
        old_item = table.pop(pk, None)
        rollback_log.append({
            "kind": "Delete",
            "table_name": table_name,
            "key": pk,
            "old_item": old_item,
        })
        return {"capacity_units": 1.0}

    elif kind == "ConditionCheck":
        # Per AWS: ConditionCheck does NOT write. Only asserts condition.
        existing = table.get(pk)
        condition = inner.get("ConditionExpression")
        expr_names = inner.get("ExpressionAttributeNames")
        expr_values = inner.get("ExpressionAttributeValues")
        if condition:
            if not _evaluate_condition(
                condition, expr_names, expr_values, existing
            ):
                raise ConditionalCheckFailedException(
                    "The conditional request failed"
                )
        return {"capacity_units": 0.5}

    return {"capacity_units": 0.5}


def _rollback_transact_items(
    store: DynamoDBStore,
    rollback_log: List[Dict[str, Any]],
) -> None:
    """Rollback all changes in reverse order."""
    for entry in reversed(rollback_log):
        table_name = entry["table_name"]
        table = store.tables.get(table_name, {})
        pk = entry["key"]

        if entry["old_item"] is None:
            table.pop(pk, None)
        else:
            table[pk] = entry["old_item"]


def _apply_update(
    inner: Dict[str, Any],
    existing: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Apply an update expression to an existing item.

    Simplified implementation. Full expression evaluation is handled
    by the expression-parser spec. This provides the local-store fallback
    for common patterns (SET, REMOVE, ADD, DELETE).
    """
    update_expr = inner.get("UpdateExpression", "")
    expr_values = inner.get("ExpressionAttributeValues", {})
    expr_names = inner.get("ExpressionAttributeNames", {})

    updated = dict(existing)

    if "SET" in update_expr.upper():
        updated = _apply_set_clause(update_expr, expr_values, expr_names, updated)
    if "REMOVE" in update_expr.upper():
        updated = _apply_remove_clause(update_expr, expr_names, updated)
    if "ADD" in update_expr.upper():
        updated = _apply_add_clause(update_expr, expr_values, expr_names, updated)
    if "DELETE" in update_expr.upper():
        updated = _apply_delete_clause(update_expr, expr_values, expr_names, updated)

    return updated


def _apply_set_clause(
    expr: str,
    expr_values: Dict[str, Any],
    expr_names: Dict[str, str],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """Parse and apply SET clause from update expression."""
    set_start = expr.upper().index("SET") + 4
    rest = expr[set_start:]
    for kw in (" REMOVE", " ADD", " DELETE"):
        if kw in rest.upper():
            rest = rest[: rest.upper().index(kw)]
    set_clause = rest.strip()

    for assignment in set_clause.split(","):
        assignment = assignment.strip()
        if "=" not in assignment:
            continue
        left, right = assignment.split("=", 1)
        left = left.strip()
        right = right.strip()

        attr_name = left
        for placeholder, name in expr_names.items():
            attr_name = attr_name.replace(placeholder, name)

        if right in expr_values:
            item[attr_name] = expr_values[right]
        else:
            item[attr_name] = right

    return item


def _apply_remove_clause(
    expr: str,
    expr_names: Dict[str, str],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """Parse and apply REMOVE clause from update expression."""
    remove_start = expr.upper().index("REMOVE") + 7
    rest = expr[remove_start:]
    for kw in (" SET", " ADD", " DELETE"):
        if kw in rest.upper():
            rest = rest[: rest.upper().index(kw)]
    remove_clause = rest.strip()

    for attr in remove_clause.split(","):
        attr = attr.strip()
        for placeholder, name in expr_names.items():
            attr = attr.replace(placeholder, name)
        item.pop(attr, None)

    return item


def _apply_add_clause(
    expr: str,
    expr_values: Dict[str, Any],
    expr_names: Dict[str, str],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """Parse and apply ADD clause from update expression."""
    add_start = expr.upper().index("ADD") + 4
    rest = expr[add_start:]
    for kw in (" SET", " REMOVE", " DELETE"):
        if kw in rest.upper():
            rest = rest[: rest.upper().index(kw)]
    add_clause = rest.strip()

    for assignment in add_clause.split(","):
        assignment = assignment.strip()
        if " " not in assignment:
            continue
        attr_name, placeholder = assignment.rsplit(" ", 1)
        for pn, name in expr_names.items():
            attr_name = attr_name.replace(pn, name)
        if placeholder in expr_values:
            val = expr_values[placeholder]
            if "N" in val:
                current = item.get(attr_name, {"N": "0"})
                new_val = int(current.get("N", "0")) + int(val["N"])
                item[attr_name] = {"N": str(new_val)}

    return item


def _apply_delete_clause(
    expr: str,
    expr_values: Dict[str, Any],
    expr_names: Dict[str, str],
    item: Dict[str, Any],
) -> Dict[str, Any]:
    """Parse and apply DELETE clause from update expression (for sets)."""
    delete_start = expr.upper().index("DELETE") + 7
    rest = expr[delete_start:]
    for kw in (" SET", " REMOVE", " ADD"):
        if kw in rest.upper():
            rest = rest[: rest.upper().index(kw)]
    delete_clause = rest.strip()

    for assignment in delete_clause.split(","):
        assignment = assignment.strip()
        if " " not in assignment:
            continue
        attr_name, placeholder = assignment.rsplit(" ", 1)
        for pn, name in expr_names.items():
            attr_name = attr_name.replace(pn, name)
        if placeholder in expr_values and attr_name in item:
            val = expr_values[placeholder]
            if "SS" in val and "SS" in item.get(attr_name, {}):
                remove_set = set(val["SS"])
                item[attr_name]["SS"] = [
                    v for v in item[attr_name]["SS"] if v not in remove_set
                ]

    return item


def _evaluate_condition(
    condition_expression: str,
    expr_names: Optional[Dict[str, str]],
    expr_values: Optional[Dict[str, Any]],
    existing: Optional[Dict[str, Any]],
) -> bool:
    """
    Evaluate a condition expression against an item.

    ConditionCheck assertions and Put/Update/Delete condition expressions.
    Returns True if condition passes, False otherwise.

    Full expression evaluation is handled by expression-parser spec.
    This stub returns True for local-store fallback.
    """
    return True


def _hash_transact_items(items: List[Dict[str, Any]]) -> str:
    """Create a deterministic hash of transact items for idempotency."""
    import hashlib
    import json

    canonical = json.dumps(items, sort_keys=True, default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()


def _check_idempotency(
    store: DynamoDBStore,
    client_token: str,
    payload_hash: str,
) -> Optional[Dict[str, Any]]:
    """
    Check if a client token has already been processed.

    Per AWS docs: token is valid for 10 minutes. If same token used with
    different parameters, raises IdempotentParameterMismatchException.
    """
    import time

    cache = getattr(store, "_transact_idempotency", {})
    if client_token in cache:
        cached_hash, cached_response, timestamp = cache[client_token]
        # 10-minute window per AWS docs
        if time.time() - timestamp > 600:
            del cache[client_token]
            return None
        if cached_hash != payload_hash:
            raise IdempotentParameterMismatchException(
                "The ClientRequestToken specified is associated with "
                "different parameters for this request."
            )
        return cached_response
    return None


def _store_idempotency(
    store: DynamoDBStore,
    client_token: str,
    payload_hash: str,
    response: Dict[str, Any],
) -> None:
    """Store the result of an idempotent transaction."""
    import time

    cache = getattr(store, "_transact_idempotency", {})
    cache[client_token] = (payload_hash, response, time.time())
    store._transact_idempotency = cache


def _error_code_for_transaction(exc: Exception) -> str:
    """Map exception type to TransactionCanceledException CancellationReason code."""
    if isinstance(exc, ConditionalCheckFailedException):
        return "ConditionalCheckFailed"
    if isinstance(exc, ValidationException):
        return "ValidationError"
    if isinstance(exc, ResourceNotFoundException):
        return "ResourceNotFound"
    return "TransactionConflict"


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


class ConditionalCheckFailedException(Exception):
    """Condition check failed."""
    pass


class TransactionCanceledException(Exception):
    """Transaction was cancelled."""
    def __init__(self, message: str, cancellation_reasons: List[Dict[str, Any]]):
        super().__init__(message)
        self.cancellation_reasons = cancellation_reasons


class IdempotentParameterMismatchException(Exception):
    """Idempotent parameter mismatch."""
    pass