---
id: "@specs/aws/dynamodb/delete-table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, table-management]
short: "DeleteTable — Deletes a table and all of its items"
---

# DeleteTable

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

The `DeleteTable` operation deletes a table and all of its items. After a `DeleteTable` request, the specified table is in the `DELETING` state until DynamoDB completes the deletion. If the table is in the `ACTIVE` state, you can delete it. If a table is in `CREATING` or `UPDATING` states, then DynamoDB returns a `ResourceInUseException`. If the specified table does not exist, DynamoDB returns a `ResourceNotFoundException`. If table is already in the `DELETING` state, no error is returned. When you delete a table, any indexes on that table are also deleted.

**Required:** TableName
**Input shape:** DeleteTableInput
**Output shape:** DeleteTableOutput

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/delete-table
# spec:implements: @kind:operation DeleteTable

def delete_table(store: DynamoDBStore, request: dict) -> dict:
    """
    Deletes a DynamoDB table and returns its TableDescription.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteTable.html

    Required fields: TableName
    Output: {TableDescription: {...}}
    Errors: ResourceInUseException, ResourceNotFoundException, LimitExceededException,
            InternalServerError
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    table_name = request['TableName']

    # --- Check table exists ---
    if not store.table_exists(table_name):
        raise ResourceNotFoundException(f"Table {table_name} not found")

    table_desc = store.get_table_description(table_name)
    status = table_desc.get('TableStatus', '')

    # --- Check table state ---
    # If table is already DELETING, no error is returned
    if status == 'DELETING':
        return {'TableDescription': table_desc}

    # If table is CREATING or UPDATING, return ResourceInUseException
    if status in ('CREATING', 'UPDATING'):
        raise ResourceInUseException(
            f"Table {table_name} is in {status} state, cannot delete"
        )

    # --- Delete the table (also removes indexes) ---
    table_desc['TableStatus'] = 'DELETING'
    store.delete_table(table_name)

    return {
        'TableDescription': table_desc,
    }
```
