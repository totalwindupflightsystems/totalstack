---
id: "@specs/aws/dynamodb/describe-table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, table-management]
short: "DescribeTable — Returns information about the table"
---

# DescribeTable

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table. If you issue a `DescribeTable` request immediately after a `CreateTable` request, DynamoDB might return a `ResourceNotFoundException`. This is because `DescribeTable` uses an eventually consistent query, and the metadata for your table might not be available at that moment.

**Required:** TableName
**Input shape:** DescribeTableInput
**Output shape:** DescribeTableOutput

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/describe-table
# spec:implements: @kind:operation DescribeTable

def describe_table(store: DynamoDBStore, request: dict) -> dict:
    """
    Returns full table metadata including status, key schema, indexes,
    throughput settings, and stream configuration.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html

    Required fields: TableName
    Output: {Table: {...}}
    Errors: ResourceNotFoundException, InternalServerError
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    table_name = request['TableName']

    # --- Check table exists ---
    if not store.table_exists(table_name):
        raise ResourceNotFoundException(f"Table {table_name} not found")

    table_desc = store.get_table_description(table_name)

    # Return the full table description wrapped in the 'Table' key
    # as per the AWS DescribeTableOutput shape
    return {
        'Table': table_desc,
    }
```
