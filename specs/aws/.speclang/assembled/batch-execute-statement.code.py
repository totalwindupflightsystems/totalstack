
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/batch-execute-statement
# spec:implements: @kind:operation BatchExecuteStatement

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def batch_execute_statement(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    statements: List[Dict[str, Any]],
    *,
    return_consumed_capacity: Optional[str] = "NONE",
) -> Dict[str, Any]:
    """
    Execute multiple PartiQL statements as a batch.


    Per AWS docs:
    - Up to 25 statements per batch.
    - Each SELECT must specify equality condition on all key attributes
      → at most 1 item returned per statement.
    - Entire batch must be all reads or all writes (cannot mix).
    - No atomicity across statements — errors are per-statement.
    - HTTP 200 may still contain per-statement errors in Responses[].Error.
    - Each statement entry: Statement, Parameters, ConsistentRead,
      ReturnValuesOnConditionCheckFailure.
    """
    # Validate statements
    if not statements:
        raise ValidationException(
            "1 validation error detected: "
            "Value '[]' at 'statements' failed to satisfy constraint: "
            "Member must have length greater than or equal to 1"
        )

    if len(statements) > 25:
        raise ValidationException(
            "1 validation error detected: "
            "Value at 'statements' failed to satisfy constraint: "
            "Member must have length less than or equal to 25"
        )

    # Validate all statements are same type (all reads or all writes)
    all_reads = True
    all_writes = True
    for stmt_entry in statements:
        stmt_text = stmt_entry.get("Statement", "")
        stmt_upper = stmt_text.strip().upper()
        if stmt_upper.startswith("SELECT"):
            all_writes = False
        else:
            all_reads = False

    if not all_reads and not all_writes:
        raise ValidationException(
            "The entire batch must consist of either read statements "
            "or write statements, you cannot mix both in one batch."
        )

    # Execute each statement independently — per AWS, errors don't fail the batch
    responses: List[Dict[str, Any]] = []
    consumed_capacity_total = 0.0
    tables_touched: Dict[str, float] = {}

    for stmt_entry in statements:
        stmt_text = stmt_entry.get("Statement", "")
        params = stmt_entry.get("Parameters", [])
        consistent_read = stmt_entry.get("ConsistentRead", False)

        try:
            result = _execute_single_statement(
                store, stmt_text, params, consistent_read,
            )
            responses.append(result)

            # Track consumed capacity per table
            table_name = result.get("TableName")
            if table_name:
                cu = result.get("ConsumedCapacity", {}).get("CapacityUnits", 1.0)
                tables_touched[table_name] = tables_touched.get(table_name, 0) + cu
                consumed_capacity_total += cu

        except Exception as exc:
            # Per AWS docs: per-statement errors are included in the response
            # as an Error field, NOT by failing the entire batch
            error_entry: Dict[str, Any] = {
                "Error": {
                    "Code": _error_code_for(exc),
                    "Message": str(exc),
                }
            }
            responses.append(error_entry)

    # Build response
    response: Dict[str, Any] = {
        "Responses": responses,
    }

    if return_consumed_capacity != "NONE" and tables_touched:
        response["ConsumedCapacity"] = [
            {
                "TableName": tn,
                "CapacityUnits": round(cu, 2),
            }
            for tn, cu in sorted(tables_touched.items())
        ]

    return response


def _execute_single_statement(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    consistent_read: bool,
) -> Dict[str, Any]:
    """
    Execute a single PartiQL statement for batch mode.

    Per AWS docs, each SELECT must specify equality on all key attributes,
    returning at most one item. This local-store implementation handles
    common patterns for SELECT, INSERT, UPDATE, DELETE.
    """
    if not statement or not statement.strip():
        raise ValidationException("Statement must not be empty")

    parameters = parameters or []
    stmt_upper = statement.strip().upper()

    if stmt_upper.startswith("SELECT"):
        return _batch_select(store, statement, parameters, consistent_read)

    elif stmt_upper.startswith("INSERT"):
        return _batch_insert(store, statement, parameters)

    elif stmt_upper.startswith("UPDATE"):
        return _batch_update(store, statement, parameters)

    elif stmt_upper.startswith("DELETE"):
        return _batch_delete(store, statement, parameters)

    else:
        raise ValidationException(
            f"Unsupported PartiQL statement type"
        )


def _batch_select(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    consistent_read: bool,
) -> Dict[str, Any]:
    """
    Execute a SELECT in batch mode.

    Per AWS: each SELECT in BatchExecuteStatement must have equality
    condition on ALL key attributes → returns at most 1 item.
    """
    table_name = _extract_table_from_partiql(statement, "FROM")
    if not table_name:
        raise ValidationException("Could not determine table name")

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    key_schema = table_def.get("KeySchema", [])
    table = store.tables.get(table_name, {})
    all_items = list(table.values())

    # Apply WHERE filtering — must match exactly one item per AWS
    filtered = _apply_partiql_where(statement, parameters, all_items)

    # Per AWS batch semantics: at most 1 item per SELECT
    item = filtered[0] if filtered else {}

    return {
        "Item": item,
        "TableName": table_name,
        "ConsumedCapacity": {
            "TableName": table_name,
            "CapacityUnits": 0.5,
        },
    }


def _batch_insert(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
) -> Dict[str, Any]:
    """Execute an INSERT in batch mode."""
    table_name = _extract_table_from_partiql(statement, "INTO")
    if not table_name:
        raise ValidationException("Could not determine table name")

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.setdefault(table_name, {})
    key_schema = table_def.get("KeySchema", [])

    item = _parse_partiql_values(statement, parameters, table_def)
    pk = _extract_primary_key(item, key_schema)

    if pk in table:
        raise ConditionalCheckFailedException("Duplicate primary key exists")

    table[pk] = item

    return {
        "TableName": table_name,
        "ConsumedCapacity": {
            "TableName": table_name,
            "CapacityUnits": 1.0,
        },
    }


def _batch_update(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
) -> Dict[str, Any]:
    """Execute an UPDATE in batch mode."""
    table_name = _extract_table_from_partiql(statement, "UPDATE")
    if not table_name:
        raise ValidationException("Could not determine table name")

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.get(table_name, {})

    # Find matching items via WHERE clause
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

    return {
        "TableName": table_name,
        "ConsumedCapacity": {
            "TableName": table_name,
            "CapacityUnits": 1.0,
        },
    }


def _batch_delete(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
) -> Dict[str, Any]:
    """Execute a DELETE in batch mode."""
    table_name = _extract_table_from_partiql(statement, "FROM")
    if not table_name:
        raise ValidationException("Could not determine table name")

    table_def = store.table_definitions.get(table_name)
    if not table_def:
        raise ResourceNotFoundException(
            f"Requested resource not found: Table: {table_name} not found"
        )

    table = store.tables.get(table_name, {})

    # Find matching items via WHERE clause
    all_items = list(table.items())
    matching = _apply_partiql_where(statement, parameters, [
        dict(item, __pk__=pk) for pk, item in all_items
    ])

    for match in matching:
        pk = match.pop("__pk__", None)
        if pk is not None:
            table.pop(pk, None)

    return {
        "TableName": table_name,
        "ConsumedCapacity": {
            "TableName": table_name,
            "CapacityUnits": 1.0,
        },
    }


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


def _error_code_for(exc: Exception) -> str:
    """Map an exception type to a DynamoDB error code string."""
    if isinstance(exc, ResourceNotFoundException):
        return "ResourceNotFoundException"
    if isinstance(exc, ValidationException):
        return "ValidationException"
    if isinstance(exc, ConditionalCheckFailedException):
        return "ConditionalCheckFailedException"
    if isinstance(exc, ProvisionedThroughputExceededException):
        return "ProvisionedThroughputExceededException"
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


class ProvisionedThroughputExceededException(Exception):
    """Provisioned throughput exceeded."""
    pass
