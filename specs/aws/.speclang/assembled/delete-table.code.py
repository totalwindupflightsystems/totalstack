
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
