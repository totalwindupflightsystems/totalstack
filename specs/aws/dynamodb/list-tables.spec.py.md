---
id: "@specs/aws/dynamodb/list-tables"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, table-management]
short: "ListTables — Returns an array of table names with pagination"
---

# ListTables

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Returns an array of table names associated with the current account and endpoint. The output from `ListTables` is paginated, with each page returning a maximum of 100 table names.

**Required:** (none)
**Input shape:** ListTablesInput
**Output shape:** ListTablesOutput

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/list-tables
# spec:implements: @kind:operation ListTables

def list_tables(store: DynamoDBStore, request: dict) -> dict:
    """
    Returns paginated list of table names.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListTables.html

    Optional fields: ExclusiveStartTableName, Limit
    Output: {TableNames: [...], LastEvaluatedTableName: "..."}
    Errors: InternalServerError
    """
    # --- Optional parameters ---
    exclusive_start = request.get('ExclusiveStartTableName')
    limit = request.get('Limit', 100)

    # --- Validate limit ---
    if limit is not None:
        if not isinstance(limit, int) or limit < 1:
            raise ValidationException(
                f"Limit must be a positive integer, got: {limit}"
            )

    # --- Get all table names from store (sorted for predictability) ---
    all_table_names = sorted(store.list_table_names())

    # --- Apply ExclusiveStartTableName pagination ---
    if exclusive_start:
        # Find the position after exclusive_start
        try:
            idx = all_table_names.index(exclusive_start)
            all_table_names = all_table_names[idx + 1:]
        except ValueError:
            # If the table name isn't found, return empty list
            all_table_names = []

    # --- Apply Limit ---
    last_evaluated = None
    if limit and len(all_table_names) > limit:
        last_evaluated = all_table_names[limit - 1]
        all_table_names = all_table_names[:limit]

    response = {
        'TableNames': all_table_names,
    }

    if last_evaluated:
        response['LastEvaluatedTableName'] = last_evaluated

    return response
```
