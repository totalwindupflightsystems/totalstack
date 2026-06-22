
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/execute-transaction
# spec:implements: @kind:operation ExecuteTransaction

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def execute_transaction(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    transact_statements: List[Dict[str, Any]],
    *,
    client_request_token: Optional[str] = None,
    return_consumed_capacity: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Execute a set of PartiQL statements as an atomic transaction.


    Per AWS docs:
    - All-or-nothing: all statements succeed or all fail together.
    - Entire transaction must be all reads or all writes (EXISTS is exception).
    - ClientRequestToken for idempotency (10-minute window).
    - Each statement has Statement, Parameters, ReturnValuesOnConditionCheckFailure.
    - If any statement fails → TransactionCanceledException with CancellationReasons.
    - Responses array: one entry per statement in order.
    """
    # Validate transact statements
    if not transact_statements:
        raise ValidationException(
            "1 validation error detected: "
            "Value '[]' at 'transactStatements' failed to satisfy constraint: "
            "Member must have length greater than or equal to 1"
        )

    # Check idempotency
    if client_request_token:
        payload_hash = _hash_statements(transact_statements)
        cached = _check_idempotency(store, client_request_token, payload_hash)
        if cached is not None:
            return cached

    # Validate all statements are same type (all reads or all writes)
    # Per AWS: entire transaction must consist of either read or write statements
    all_reads = True
    all_writes = True
    for stmt_entry in transact_statements:
        stmt = stmt_entry.get("Statement", "")
        stmt_upper = stmt.strip().upper()
        if stmt_upper.startswith("SELECT") or stmt_upper.startswith("EXISTS"):
            all_writes = False
        else:
            all_reads = False

    if not all_reads and not all_writes:
        raise ValidationException(
            "Transaction statements must be all reads or all writes"
        )

    # Execute statements in order with rollback capability
    results: List[Dict[str, Any]] = []
    rollback_log: List[Dict[str, Any]] = []
    consumed_capacity_total = 0.0
    tables_touched: Dict[str, float] = {}

    try:
        for idx, stmt_entry in enumerate(transact_statements):
            statement = stmt_entry.get("Statement", "")
            parameters = stmt_entry.get("Parameters", [])

            if not statement.strip():
                raise ValidationException("Statement must not be empty")

            result = _execute_partiql_transaction_statement(
                store, statement, parameters, rollback_log
            )
            results.append(result)

            table_name = result.get("table_name")
            if table_name:
                tables_touched[table_name] = (
                    tables_touched.get(table_name, 0)
                    + result.get("capacity_units", 1.0)
                )
                consumed_capacity_total += result.get("capacity_units", 1.0)

    except Exception as exc:
        # Rollback all prior statements in reverse order
        _rollback_transaction(store, rollback_log)

        raise TransactionCanceledException(
            f"Transaction cancelled, {exc}",
            [
                {"Code": _error_code_for(exc), "Message": str(exc)}
            ],
        )

    # Build response
    response: Dict[str, Any] = {
        "Responses": results,
    }

    if return_consumed_capacity != "NONE" and tables_touched:
        response["ConsumedCapacity"] = [
            {
                "TableName": tn,
                "CapacityUnits": round(cu, 2),
            }
            for tn, cu in sorted(tables_touched.items())
        ]

    # Cache idempotency result
    if client_request_token:
        _store_idempotency(store, client_request_token, payload_hash, response)

    return response


def _execute_partiql_transaction_statement(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    rollback_log: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Execute a single PartiQL statement within a transaction.

    Parses the statement to determine operation type and applies it.
    Returns a response dict for inclusion in the Responses array.
    """
    stmt_upper = statement.strip().upper()

    if stmt_upper.startswith("SELECT") or stmt_upper.startswith("EXISTS"):
        return _partiql_select_transaction(store, statement, parameters)

    elif stmt_upper.startswith("INSERT"):
        return _partiql_insert_transaction(
            store, statement, parameters, rollback_log
        )

    elif stmt_upper.startswith("UPDATE"):
        return _partiql_update_transaction(
            store, statement, parameters, rollback_log
        )

    elif stmt_upper.startswith("DELETE"):
        return _partiql_delete_transaction(
            store, statement, parameters, rollback_log
        )

    else:
        raise ValidationException(
            f"Unsupported PartiQL statement: {statement[:80]}"
        )


def _partiql_select_transaction(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
) -> Dict[str, Any]:
    """Execute a SELECT statement within a transaction."""
    table_name = _extract_table_from_partiql(statement, "FROM")
    if not table_name:
        raise ValidationException(
            "Could not determine table name from SELECT statement"
        )

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.get(table_name, {})
    items = list(table.values())

    # Apply WHERE filtering
    filtered = _apply_partiql_where(statement, parameters, items)

    return {
        "Item": filtered[0] if filtered else {},
        "table_name": table_name,
        "capacity_units": 0.5,
    }


def _partiql_insert_transaction(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    rollback_log: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Execute an INSERT statement within a transaction."""
    table_name = _extract_table_from_partiql(statement, "INTO")
    if not table_name:
        raise ValidationException(
            "Could not determine table name from INSERT statement"
        )

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.setdefault(table_name, {})

    item = _parse_partiql_values(statement, parameters, table_def)
    key_schema = table_def.get("KeySchema", [])
    pk = _extract_primary_key(item, key_schema)

    old_item = table.get(pk)
    table[pk] = item

    rollback_log.append({
        "kind": "INSERT",
        "table_name": table_name,
        "key": pk,
        "old_item": old_item,
    })

    return {
        "table_name": table_name,
        "capacity_units": 1.0,
    }


def _partiql_update_transaction(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    rollback_log: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Execute an UPDATE statement within a transaction."""
    table_name = _extract_table_from_partiql(statement, "UPDATE")
    if not table_name:
        raise ValidationException(
            "Could not determine table name from UPDATE statement"
        )

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.get(table_name, {})
    key_schema = table_def.get("KeySchema", [])

    # Find matching items via WHERE and update them
    all_items = list(table.items())
    matching = _apply_partiql_where(statement, parameters, [
        dict(item, __pk__=pk) for pk, item in all_items
    ])

    for match in matching:
        pk = match.pop("__pk__", None)
        if pk is None:
            continue
        old_item = table.get(pk)
        if old_item is not None:
            updated = _apply_partiql_set(statement, parameters, old_item)
            table[pk] = updated
            rollback_log.append({
                "kind": "UPDATE",
                "table_name": table_name,
                "key": pk,
                "old_item": old_item,
            })

    return {
        "table_name": table_name,
        "capacity_units": 1.0,
    }


def _partiql_delete_transaction(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    rollback_log: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Execute a DELETE statement within a transaction."""
    table_name = _extract_table_from_partiql(statement, "FROM")
    if not table_name:
        raise ValidationException(
            "Could not determine table name from DELETE statement"
        )

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.get(table_name, {})

    # Find matching items via WHERE and delete them
    all_items = list(table.items())
    matching = _apply_partiql_where(statement, parameters, [
        dict(item, __pk__=pk) for pk, item in all_items
    ])

    for match in matching:
        pk = match.pop("__pk__", None)
        if pk is not None:
            old_item = table.pop(pk, None)
            rollback_log.append({
                "kind": "DELETE",
                "table_name": table_name,
                "key": pk,
                "old_item": old_item,
            })

    return {
        "table_name": table_name,
        "capacity_units": 1.0,
    }


def _rollback_transaction(
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


def _extract_table_from_partiql(statement: str, keyword: str) -> Optional[str]:
    """Extract the table name from a PartiQL statement after a keyword."""
    import re

    stmt_upper = statement.upper()
    idx = stmt_upper.find(keyword)
    if idx == -1:
        return None

    after_kw = statement[idx + len(keyword):].strip()
    match = re.match(r'"([^"]+)"|(\S+)', after_kw)
    if match:
        return match.group(1) or match.group(2)
    return None


def _parse_partiql_values(
    statement: str,
    parameters: List[Any],
    table_def: Dict[str, Any],
) -> Dict[str, Any]:
    """Parse the VALUES clause of an INSERT into a DynamoDB item."""
    item: Dict[str, Any] = {}
    key_schema = table_def.get("KeySchema", [])

    for i, key_elem in enumerate(key_schema):
        attr_name = key_elem["AttributeName"]
        if i < len(parameters):
            val = parameters[i]
            if isinstance(val, str):
                item[attr_name] = {"S": val}
            elif isinstance(val, (int, float)):
                item[attr_name] = {"N": str(val)}
            elif isinstance(val, dict):
                item[attr_name] = val

    return item


def _apply_partiql_where(
    statement: str,
    parameters: List[Any],
    items: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Apply PartiQL WHERE clause filtering (simplified)."""
    import re

    where_match = re.search(
        r'WHERE\s+(.+?)(?:\s+ORDER|\s+LIMIT|\s*$)', statement, re.IGNORECASE
    )
    if not where_match:
        return items

    where_clause = where_match.group(1).strip()
    eq_match = re.match(r'(\w+)\s*=\s*\?', where_clause.strip())
    if eq_match:
        attr_name = eq_match.group(1)
        parts_before = statement[:where_match.start()].count("?")
        if parts_before < len(parameters):
            val = parameters[parts_before]
            filtered = []
            for item in items:
                if attr_name in item:
                    attr_val = item[attr_name]
                    if "S" in attr_val and isinstance(val, str):
                        if attr_val["S"] == val:
                            filtered.append(item)
                    elif "N" in attr_val and isinstance(val, (int, float)):
                        if float(attr_val["N"]) == float(val):
                            filtered.append(item)
            return filtered

    return items


def _apply_partiql_set(
    statement: str,
    parameters: List[Any],
    existing: Dict[str, Any],
) -> Dict[str, Any]:
    """Apply PartiQL UPDATE SET clause."""
    import re

    updated = dict(existing)
    set_match = re.search(
        r'SET\s+(.+?)(?:\s+WHERE|\s*$)', statement, re.IGNORECASE
    )
    if not set_match:
        return updated

    set_clause = set_match.group(1).strip()
    assignments = re.findall(
        r'(\w+)\s*=\s*(\?)', set_clause, re.IGNORECASE
    )

    where_pos = statement.upper().find("WHERE")
    before_section = statement[:where_pos] if where_pos > 0 else statement
    set_start = before_section.upper().find("SET")
    params_before_set = before_section[:set_start].count("?") if set_start >= 0 else 0

    for i, (attr_name, _) in enumerate(assignments):
        param_idx = params_before_set + i
        if param_idx < len(parameters):
            val = parameters[param_idx]
            if isinstance(val, str):
                updated[attr_name] = {"S": val}
            elif isinstance(val, (int, float)):
                updated[attr_name] = {"N": str(val)}
            elif isinstance(val, dict):
                updated[attr_name] = val

    return updated


def _extract_primary_key(
    item: Dict[str, Any],
    key_schema: List[Dict[str, str]],
) -> str:
    """Extract a string representation of the primary key from an item."""
    parts = []
    for key_elem in key_schema:
        attr_name = key_elem["AttributeName"]
        if attr_name in item:
            attr_value = item[attr_name]
            if "S" in attr_value:
                parts.append(attr_value["S"])
            elif "N" in attr_value:
                parts.append(str(attr_value["N"]))
            elif "B" in attr_value:
                parts.append(attr_value["B"])
    return "|".join(parts)


def _hash_statements(statements: List[Dict[str, Any]]) -> str:
    """Create a deterministic hash of statements for idempotency."""
    import hashlib
    import json

    canonical = json.dumps(statements, sort_keys=True, default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()


def _check_idempotency(
    store: DynamoDBStore,
    client_token: str,
    payload_hash: str,
) -> Optional[Dict[str, Any]]:
    """Check if a client token has already been processed (10-min window per AWS)."""
    import time

    cache = getattr(store, "_partiql_txn_idempotency", {})
    if client_token in cache:
        cached_hash, cached_response, ts = cache[client_token]
        if time.time() - ts > 600:
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

    cache = getattr(store, "_partiql_txn_idempotency", {})
    cache[client_token] = (payload_hash, response, time.time())
    store._partiql_txn_idempotency = cache


def _error_code_for(exc: Exception) -> str:
    """Map exception to error code string."""
    if isinstance(exc, ResourceNotFoundException):
        return "ResourceNotFoundException"
    if isinstance(exc, ValidationException):
        return "ValidationException"
    if isinstance(exc, ConditionalCheckFailedException):
        return "ConditionalCheckFailedException"
    return "InternalServerError"


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
