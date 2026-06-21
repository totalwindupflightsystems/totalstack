---
id: "@specs/aws/dynamodb/delete-item"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, item-crud]
short: "DeleteItem — Deletes a single item in a table by primary key"
---

# DeleteItem

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Deletes a single item in a table by primary key. You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected attribute value. In addition to deleting an item, you can also return the item's attribute values in the same operation, using the `ReturnValues` parameter. Unless you specify conditions, the `DeleteItem` is an idempotent operation; running it multiple times on the same item or attribute does *not* result in an error response.

**Required:** TableName, Key
**Input shape:** DeleteItemInput
**Output shape:** DeleteItemOutput

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/delete-item
# spec:implements: @kind:operation DeleteItem

def delete_item(store: DynamoDBStore, request: dict) -> dict:
    """
    Deletes a single item from a DynamoDB table by primary key.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html

    Required fields: TableName, Key
    Output: {Attributes?: {...}, ConsumedCapacity?: {...}, ItemCollectionMetrics?: {...}}
    Errors: ConditionalCheckFailedException, ProvisionedThroughputExceededException,
            ResourceNotFoundException, ItemCollectionSizeLimitExceededException,
            TransactionConflictException, RequestLimitExceeded, InternalServerError,
            ReplicatedWriteConflictException, ThrottlingException
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    if 'Key' not in request or not request['Key']:
        raise ValidationException("Key is required")

    table_name = request['TableName']
    key = request['Key']
    return_values = request.get('ReturnValues', 'NONE')
    condition_expression = request.get('ConditionExpression')
    expression_attribute_names = request.get('ExpressionAttributeNames', {})
    expression_attribute_values = request.get('ExpressionAttributeValues', {})
    return_consumed_capacity = request.get('ReturnConsumedCapacity')
    return_item_collection_metrics = request.get('ReturnItemCollectionMetrics')

    # --- Validate ReturnValues ---
    # DeleteItem only supports NONE and ALL_OLD
    valid_return_values = ('NONE', 'ALL_OLD')
    if return_values not in valid_return_values:
        raise ValidationException(
            f"ReturnValues for DeleteItem must be one of {valid_return_values}, "
            f"got: {return_values}"
        )

    # --- Validate ReturnItemCollectionMetrics ---
    if return_item_collection_metrics:
        valid_metrics = ('SIZE', 'NONE')
        if return_item_collection_metrics not in valid_metrics:
            raise ValidationException(
                f"ReturnItemCollectionMetrics must be one of {valid_metrics}, "
                f"got: {return_item_collection_metrics}"
            )

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

    # --- Get existing item for conditional checks and ReturnValues ---
    existing_item = store.get_item(table_name, key)

    # --- Idempotent: if item doesn't exist (and no condition), no error ---
    if existing_item is None and not condition_expression:
        response = {}
        if return_consumed_capacity:
            response['ConsumedCapacity'] = _compute_consumed_capacity({}, return_consumed_capacity)
        return response

    # --- Handle conditional delete ---
    if condition_expression:
        if not _evaluate_condition(
            existing_item, condition_expression,
            expression_attribute_names, expression_attribute_values
        ):
            raise ConditionalCheckFailedException(
                "The conditional request failed"
            )

    # --- Perform the delete ---
    if existing_item is not None:
        store.delete_item(table_name, key)

    # --- Build response ---
    response = {}

    if return_values == 'ALL_OLD' and existing_item:
        response['Attributes'] = existing_item

    if return_consumed_capacity:
        response['ConsumedCapacity'] = _compute_consumed_capacity(
            existing_item or {}, return_consumed_capacity
        )

    if return_item_collection_metrics == 'SIZE':
        response['ItemCollectionMetrics'] = _compute_item_collection_metrics(
            store, table_name, existing_item or key
        )

    return response


def _evaluate_condition(item, condition_expr, attr_names, attr_values) -> bool:
    """Evaluate a condition expression against an item (stub)."""
    return True


def _compute_consumed_capacity(item, return_mode) -> dict:
    """Compute consumed capacity for the operation."""
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
```
