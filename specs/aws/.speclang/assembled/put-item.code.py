
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/put-item
# spec:implements: @kind:operation PutItem

def put_item(store: DynamoDBStore, request: dict) -> dict:
    """
    Creates a new item or replaces an existing item in a DynamoDB table.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html

    Required fields: TableName, Item
    Output: {Attributes?: {...}, ConsumedCapacity?: {...}, ItemCollectionMetrics?: {...}}
    Errors: ConditionalCheckFailedException, ProvisionedThroughputExceededException,
            ResourceNotFoundException, ItemCollectionSizeLimitExceededException,
            TransactionConflictException, RequestLimitExceeded, InternalServerError,
            ReplicatedWriteConflictException, ThrottlingException
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    if 'Item' not in request or not request['Item']:
        raise ValidationException("Item is required")

    table_name = request['TableName']
    item = request['Item']
    return_values = request.get('ReturnValues', 'NONE')
    return_consumed_capacity = request.get('ReturnConsumedCapacity')
    return_item_collection_metrics = request.get('ReturnItemCollectionMetrics')
    condition_expression = request.get('ConditionExpression')
    expression_attribute_names = request.get('ExpressionAttributeNames', {})
    expression_attribute_values = request.get('ExpressionAttributeValues', {})

    # --- Validate ReturnValues ---
    # PutItem only supports NONE and ALL_OLD
    valid_return_values = ('NONE', 'ALL_OLD')
    if return_values not in valid_return_values:
        raise ValidationException(
            f"ReturnValues for PutItem must be one of {valid_return_values}, got: {return_values}"
        )

    # --- Validate ReturnItemCollectionMetrics ---
    if return_item_collection_metrics:
        valid_metrics = ('SIZE', 'NONE')
        if return_item_collection_metrics not in valid_metrics:
            raise ValidationException(
                f"ReturnItemCollectionMetrics must be one of {valid_metrics}, "
                f"got: {return_item_collection_metrics}"
            )

    # --- Check table exists ---
    if not store.table_exists(table_name):
        raise ResourceNotFoundException(f"Table {table_name} not found")

    table_desc = store.get_table_description(table_name)

    # --- Validate item contains all key attributes ---
    key_schema = table_desc.get('KeySchema', [])
    for key_elem in key_schema:
        key_name = key_elem['AttributeName']
        if key_name not in item:
            raise ValidationException(
                f"Missing key attribute '{key_name}' in Item"
            )

    # --- Get existing item for conditional checks and ReturnValues ---
    existing_item = store.get_item(table_name, _extract_key(item, key_schema))

    # --- Handle conditional put ---
    if condition_expression:
        if not _evaluate_condition(
            existing_item, condition_expression,
            expression_attribute_names, expression_attribute_values
        ):
            raise ConditionalCheckFailedException(
                "The conditional request failed"
            )

    # --- Perform the put ---
    store.put_item(table_name, item)

    # --- Build response ---
    response = {}

    if return_values == 'ALL_OLD' and existing_item:
        response['Attributes'] = existing_item

    if return_consumed_capacity:
        response['ConsumedCapacity'] = _compute_consumed_capacity(
            item, return_consumed_capacity
        )

    if return_item_collection_metrics == 'SIZE':
        response['ItemCollectionMetrics'] = _compute_item_collection_metrics(
            store, table_name, item
        )

    return response


def _extract_key(item: dict, key_schema: list) -> dict:
    """Extract the primary key from an item dict."""
    key = {}
    for key_elem in key_schema:
        attr_name = key_elem['AttributeName']
        if attr_name in item:
            key[attr_name] = item[attr_name]
    return key


def _evaluate_condition(item, condition_expr, attr_names, attr_values) -> bool:
    """Evaluate a condition expression against an item (stub)."""
    # Full condition expression parser is implemented in ExpressionParser component.
    # This stub always returns True for non-conditional puts.
    return True


def _compute_consumed_capacity(item, return_mode) -> dict:
    """Compute consumed capacity for the operation."""
    # For the emulator, return a placeholder
    return {
        'TableName': '',
        'CapacityUnits': 1.0,
    }


def _compute_item_collection_metrics(store, table_name, item) -> dict:
    """Compute item collection metrics."""
    return {
        'ItemCollectionKey': {},
        'SizeEstimateRangeGB': [0.0, 0.0],
    }
