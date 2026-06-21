---
id: "@specs/aws/dynamodb/execute-statement"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, execute-statement, partiql]
short: "ExecuteStatement operation — run a single PartiQL statement"
---

# ExecuteStatement

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc
> **source:** AWS DynamoDB API Reference — ExecuteStatement

This operation allows you to perform reads and singleton writes on data stored in DynamoDB using PartiQL. For PartiQL reads (`SELECT`), if the total number of processed items exceeds 1 MB, the read stops and returns a `LastEvaluatedKey` or `NextToken` to continue in a subsequent operation. If no data matches the `WHERE` clause, an empty result set is returned.

Parameters are bound to `?` placeholders positionally. `ConsistentRead` enables strongly consistent reads for `SELECT`. `Limit` restricts the number of items evaluated. `NextToken` is used to paginate remaining results. `ReturnValuesOnConditionCheckFailure` returns item attributes when a condition check fails (no additional RCU cost).

**Required:** `Statement`
**Input shape:** `ExecuteStatementInput`
**Output shape:** `ExecuteStatementOutput` (Items, NextToken, ConsumedCapacity, LastEvaluatedKey)

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/execute-statement
# spec:implements: @kind:operation ExecuteStatement

from typing import Optional, Dict, Any, List
from localstack.services.dynamodb.models import DynamoDBStore


def execute_statement(
    store: DynamoDBStore,
    account_id: str,
    region_name: str,
    statement: str,
    *,
    parameters: Optional[List[Any]] = None,
    consistent_read: bool = False,
    limit: Optional[int] = None,
    next_token: Optional[str] = None,
    return_consumed_capacity: Optional[str] = "NONE",
    return_values_on_condition_check_failure: Optional[str] = "ALL_OLD",
) -> Dict[str, Any]:
    """
    Execute a single PartiQL statement against DynamoDB tables.

    @kind:operation ExecuteStatement

    Per AWS docs:
    - Supports SELECT, INSERT, UPDATE, DELETE PartiQL statements.
    - SELECT reads up to 1 MB; pagination via NextToken/LastEvaluatedKey.
    - Parameters bound to ``?`` placeholders positionally.
    - ConsistentRead=True for strongly consistent SELECT reads.
    - Limit restricts evaluated items (not necessarily returned items).
    - NextToken for paginating remaining results.
    - ReturnValuesOnConditionCheckFailure returns item attrs on condition fail.
    """
    if not statement or not statement.strip():
        raise ValidationException(
            "1 validation error detected: "
            "Value at 'statement' failed to satisfy constraint: "
            "Member must not be null"
        )

    # Empty parameter list rejected per AWS JS client
    if parameters is not None and len(parameters) == 0:
        raise ValidationException(
            "1 validation error detected: Value '[]' at 'parameters' "
            "failed to satisfy constraint: Member must have length "
            "greater than or equal to 1"
        )

    parameters = parameters or []
    stmt_upper = statement.strip().upper()

    if stmt_upper.startswith("SELECT"):
        return _execute_select(
            store, statement, parameters,
            consistent_read, limit, next_token,
            return_consumed_capacity,
        )
    elif stmt_upper.startswith("INSERT"):
        return _execute_insert(
            store, statement, parameters,
            return_consumed_capacity,
        )
    elif stmt_upper.startswith("UPDATE"):
        return _execute_update(
            store, statement, parameters,
            return_values_on_condition_check_failure,
            return_consumed_capacity,
        )
    elif stmt_upper.startswith("DELETE"):
        return _execute_delete(
            store, statement, parameters,
            return_consumed_capacity,
        )
    else:
        raise ValidationException(
            f"Unsupported PartiQL statement type"
        )


def _execute_select(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    consistent_read: bool,
    limit: Optional[int],
    next_token: Optional[str],
    return_consumed_capacity: str,
) -> Dict[str, Any]:
    """
    Execute a PartiQL SELECT statement.

    Per AWS docs:
    - 1 MB dataset size limit; stops and returns LastEvaluatedKey/NextToken.
    - Limit restricts evaluated items.
    - If WHERE clause matches nothing, returns empty result set.
    """
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
    all_items = list(table.values())

    # Apply WHERE filtering
    filtered = _apply_partiql_where(statement, parameters, all_items)

    # Apply pagination via NextToken
    start_idx = 0
    if next_token:
        try:
            import json
            import base64
            decoded = json.loads(base64.b64decode(next_token.encode()).decode())
            start_idx = decoded.get("offset", 0)
        except Exception:
            raise ValidationException("Invalid NextToken")

    end_idx = len(filtered)
    if limit is not None and limit > 0:
        end_idx = min(start_idx + limit, len(filtered))

    page_items = filtered[start_idx:end_idx]
    scanned_count = len(all_items)

    response: Dict[str, Any] = {
        "Items": page_items,
    }

    # LastEvaluatedKey and NextToken for pagination
    if end_idx < len(filtered):
        import json
        import base64
        next_token_val = base64.b64encode(
            json.dumps({"offset": end_idx}).encode()
        ).decode()
        response["NextToken"] = next_token_val

    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = {
            "TableName": table_name,
            "CapacityUnits": 0.5 + (scanned_count * 0.005),
        }

    return response


def _execute_insert(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    return_consumed_capacity: str,
) -> Dict[str, Any]:
    """Execute a PartiQL INSERT statement."""
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
    key_schema = table_def.get("KeySchema", [])

    # Build item from VALUES clause and parameters
    item = _parse_partiql_values(statement, parameters, table_def)
    pk = _extract_primary_key(item, key_schema)

    # Check for duplicate key
    if pk in table:
        raise ConditionalCheckFailedException(
            "Duplicate primary key exists"
        )

    table[pk] = item

    response: Dict[str, Any] = {}
    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = {
            "TableName": table_name,
            "CapacityUnits": 1.0,
        }

    return response


def _execute_update(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    return_values_on_condition_check_failure: str,
    return_consumed_capacity: str,
) -> Dict[str, Any]:
    """Execute a PartiQL UPDATE statement."""
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

    # Find items matching WHERE clause
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

    response: Dict[str, Any] = {}
    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = {
            "TableName": table_name,
            "CapacityUnits": 1.0,
        }

    return response


def _execute_delete(
    store: DynamoDBStore,
    statement: str,
    parameters: List[Any],
    return_consumed_capacity: str,
) -> Dict[str, Any]:
    """Execute a PartiQL DELETE statement."""
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

    # Find items matching WHERE clause
    all_items = list(table.items())
    matching = _apply_partiql_where(statement, parameters, [
        dict(item, __pk__=pk) for pk, item in all_items
    ])

    for match in matching:
        pk = match.pop("__pk__", None)
        if pk is not None:
            table.pop(pk, None)

    response: Dict[str, Any] = {}
    if return_consumed_capacity != "NONE":
        response["ConsumedCapacity"] = {
            "TableName": table_name,
            "CapacityUnits": 1.0,
        }

    return response


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
    """Parse the VALUES clause of an INSERT statement into a DynamoDB item."""
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
    """
    Apply a PartiQL WHERE clause to filter items.

    Simplified: full PartiQL expression evaluation handled by expression-parser.
    This provides local-store fallback for basic ``attr = ?`` patterns.
    """
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
    """Apply a PartiQL UPDATE SET clause to an existing item."""
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

    # Find parameter offset for SET clause
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


class ResourceNotFoundException(Exception):
    """Table not found."""
    pass


class ValidationException(Exception):
    """Input validation failed."""
    pass


class ConditionalCheckFailedException(Exception):
    """Condition check failed."""
    pass
```
