
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/get-item
# spec:implements: @kind:operation GetItem

def get_item(store: DynamoDBStore, request: dict) -> dict:
    """
    Retrieves an item from a DynamoDB table by its primary key.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html

    Required fields: TableName, Key
    Output: {Item?: {...}, ConsumedCapacity?: {...}}
    Errors: ProvisionedThroughputExceededException, ResourceNotFoundException,
            RequestLimitExceeded, InternalServerError, ThrottlingException
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    if 'Key' not in request or not request['Key']:
        raise ValidationException("Key is required")

    table_name = request['TableName']
    key = request['Key']
    consistent_read = request.get('ConsistentRead', False)
    projection_expression = request.get('ProjectionExpression')
    expression_attribute_names = request.get('ExpressionAttributeNames', {})
    return_consumed_capacity = request.get('ReturnConsumedCapacity')

    # --- Validate Key is a dict ---
    if not isinstance(key, dict):
        raise ValidationException("Key must be a map of attribute names to AttributeValue objects")

    # --- Check table exists ---
    if not store.table_exists(table_name):
        raise ResourceNotFoundException(f"Table {table_name} not found")

    table_desc = store.get_table_description(table_name)
    key_schema = table_desc.get('KeySchema', [])

    # --- Validate key contains all key attributes ---
    for key_elem in key_schema:
        attr_name = key_elem['AttributeName']
        if attr_name not in key:
            raise ValidationException(
                f"Missing key attribute '{attr_name}' in Key"
            )

    # --- Retrieve item ---
    item = store.get_item(table_name, key)

    # --- Build response ---
    response = {}

    if item:
        # --- Apply projection expression ---
        if projection_expression:
            item = _apply_projection(item, projection_expression, expression_attribute_names)
        response['Item'] = item

    if return_consumed_capacity:
        response['ConsumedCapacity'] = _compute_consumed_capacity(
            item or {}, return_consumed_capacity
        )

    return response


def _apply_projection(item: dict, projection_expression: str, attr_names: dict) -> dict:
    """
    Apply a projection expression to filter item attributes.

    ProjectionExpression is a comma-separated list of attribute names.
    If no attribute names are specified, all attributes are returned.
    If any of the requested attributes are not found, they do not appear in the result.
    """
    if not projection_expression:
        return item

    # Split by comma, strip whitespace
    requested_attrs = [a.strip() for a in projection_expression.split(',')]
    result = {}
    for attr in requested_attrs:
        # Resolve expression attribute name placeholders (e.g., #P → Percentile)
        actual_attr = attr_names.get(attr, attr)
        if actual_attr in item:
            result[actual_attr] = item[actual_attr]

    return result


def _compute_consumed_capacity(item: dict, return_mode: str) -> dict:
    """Compute consumed capacity for the operation (emulator stub)."""
    return {
        'TableName': '',
        'CapacityUnits': 0.5,
    }
