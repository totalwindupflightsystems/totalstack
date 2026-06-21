// spec:trace spec=/home/kara/totalstack/specs/aws/dynamodb/describe-table.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

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