---
id: "@specs/aws/dynamodb/update-item"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/dynamodb/plan"
tags: [aws, dynamodb, item-crud]
short: "UpdateItem — Edits an existing item's attributes or adds a new item"
---

# UpdateItem

> **spec:trace:** specs/aws/dynamodb/dynamodb.spec.plan.md#phase-1--core-crud-poc

Edits an existing item's attributes, or adds a new item to the table if it does not already exist. You can put, delete, or add attribute values. You can also perform a conditional update on an existing item (insert a new attribute name-value pair if it doesn't exist, or replace an existing name-value pair if it has certain expected attribute values). You can also return the item's attribute values in the same `UpdateItem` operation using the `ReturnValues` parameter.

**Required:** TableName, Key
**Input shape:** UpdateItemInput
**Output shape:** UpdateItemOutput

## Implementation

```speclang
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/update-item
# spec:implements: @kind:operation UpdateItem

def update_item(store: DynamoDBStore, request: dict) -> dict:
    """
    Edits an existing item's attributes or adds a new item if it doesn't exist.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html

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
    update_expression = request.get('UpdateExpression')
    return_values = request.get('ReturnValues', 'NONE')
    condition_expression = request.get('ConditionExpression')
    expression_attribute_names = request.get('ExpressionAttributeNames', {})
    expression_attribute_values = request.get('ExpressionAttributeValues', {})
    return_consumed_capacity = request.get('ReturnConsumedCapacity')
    return_item_collection_metrics = request.get('ReturnItemCollectionMetrics')

    # --- Validate ReturnValues ---
    # UpdateItem supports: NONE, ALL_OLD, UPDATED_OLD, ALL_NEW, UPDATED_NEW
    valid_return_values = ('NONE', 'ALL_OLD', 'UPDATED_OLD', 'ALL_NEW', 'UPDATED_NEW')
    if return_values not in valid_return_values:
        raise ValidationException(
            f"ReturnValues for UpdateItem must be one of {valid_return_values}, "
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

    # --- Get existing item ---
    existing_item = store.get_item(table_name, key)
    old_item = dict(existing_item) if existing_item else None

    # --- Handle conditional update ---
    if condition_expression:
        if not _evaluate_condition(
            existing_item, condition_expression,
            expression_attribute_names, expression_attribute_values
        ):
            raise ConditionalCheckFailedException(
                "The conditional request failed"
            )

    # --- Apply update expression ---
    if existing_item is None:
        # Item doesn't exist — create it from key attributes
        existing_item = dict(key)

    if update_expression:
        updated_attrs = _apply_update_expression(
            existing_item, update_expression,
            expression_attribute_names, expression_attribute_values
        )
    else:
        updated_attrs = set()

    # --- Perform the update ---
    store.put_item(table_name, existing_item)

    # --- Build response ---
    response = {}

    if return_values != 'NONE':
        if return_values == 'ALL_OLD':
            response['Attributes'] = old_item
        elif return_values == 'ALL_NEW':
            response['Attributes'] = existing_item
        elif return_values == 'UPDATED_OLD':
            # Return only the updated attributes as they were before
            response['Attributes'] = {
                k: v for k, v in (old_item or {}).items()
                if k in updated_attrs
            }
        elif return_values == 'UPDATED_NEW':
            # Return only the updated attributes as they are now
            response['Attributes'] = {
                k: v for k, v in existing_item.items()
                if k in updated_attrs
            }

    if return_consumed_capacity:
        response['ConsumedCapacity'] = _compute_consumed_capacity(
            existing_item, return_consumed_capacity
        )

    if return_item_collection_metrics == 'SIZE':
        response['ItemCollectionMetrics'] = _compute_item_collection_metrics(
            store, table_name, existing_item
        )

    return response


def _apply_update_expression(item: dict, update_expr: str,
                              attr_names: dict, attr_values: dict) -> set:
    """
    Apply an UpdateExpression to an item.

    Supports the following actions:
    - SET: Adds/replaces attributes. Supports if_not_exists(), list_append()
    - REMOVE: Removes attributes
    - ADD: Adds to number or set attributes
    - DELETE: Removes elements from a set

    Returns the set of attribute names that were modified.
    """
    # Full update expression parser is implemented in ExpressionParser component.
    # This stub always returns an empty set of updated attributes.
    return set()


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
