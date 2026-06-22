
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/create-table
# spec:implements: @kind:operation CreateTable

def create_table(store: DynamoDBStore, request: dict) -> dict:
    """
    Creates a new DynamoDB table with the given schema, indexes, and settings.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html

    Required fields: TableName
    Output: {TableDescription: {...}}
    Errors: ResourceInUseException, LimitExceededException, InternalServerError
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    table_name = request['TableName']
    key_schema = request.get('KeySchema', [])
    attribute_defs = request.get('AttributeDefinitions', [])
    billing_mode = request.get('BillingMode', 'PROVISIONED')
    provisioned_throughput = request.get('ProvisionedThroughput')
    stream_spec = request.get('StreamSpecification')
    sse_spec = request.get('SSESpecification')
    tags = request.get('Tags', [])
    table_class = request.get('TableClass', 'STANDARD')
    deletion_protection = request.get('DeletionProtectionEnabled', False)
    lsi_list = request.get('LocalSecondaryIndexes', [])
    gsi_list = request.get('GlobalSecondaryIndexes', [])

    # --- Validate TableName uniqueness ---
    if store.table_exists(table_name):
        raise ResourceInUseException(f"Table {table_name} already exists")

    # --- Validate BillingMode ---
    valid_billing_modes = ('PAY_PER_REQUEST', 'PROVISIONED')
    if billing_mode not in valid_billing_modes:
        raise ValidationException(
            f"BillingMode must be one of {valid_billing_modes}, got: {billing_mode}"
        )

    # --- Validate BillingMode/ProvisionedThroughput consistency ---
    if billing_mode == 'PROVISIONED' and not provisioned_throughput:
        raise ValidationException(
            "ProvisionedThroughput is required when BillingMode is PROVISIONED"
        )
    if billing_mode == 'PAY_PER_REQUEST' and provisioned_throughput:
        raise ValidationException(
            "ProvisionedThroughput cannot be specified when BillingMode is PAY_PER_REQUEST"
        )

    # --- Validate KeySchema ---
    # For a simple primary key: exactly one element with KeyType=HASH
    # For a composite primary key: exactly two elements, first HASH, second RANGE
    if len(key_schema) < 1 or len(key_schema) > 2:
        raise ValidationException(
            f"KeySchema must have 1 or 2 elements, got {len(key_schema)}"
        )

    hash_count = sum(1 for k in key_schema if k.get('KeyType') == 'HASH')
    range_count = sum(1 for k in key_schema if k.get('KeyType') == 'RANGE')

    if hash_count != 1:
        raise ValidationException("KeySchema must contain exactly one HASH key element")

    if len(key_schema) == 2 and range_count != 1:
        raise ValidationException("Two-element KeySchema must contain one HASH and one RANGE key")

    # Simple primary key must have KeyType=HASH as first element
    if key_schema[0].get('KeyType') != 'HASH':
        raise ValidationException("First KeySchema element must have KeyType=HASH")

    # --- Validate AttributeDefinitions include all key attributes ---
    attr_def_names = {a['AttributeName'] for a in attribute_defs}
    for key in key_schema:
        attr_name = key.get('AttributeName', '')
        if attr_name not in attr_def_names:
            raise ValidationException(
                f"Attribute '{attr_name}' in KeySchema must be defined in AttributeDefinitions"
            )

    # --- Validate TableClass ---
    valid_table_classes = ('STANDARD', 'STANDARD_INFREQUENT_ACCESS')
    if table_class not in valid_table_classes:
        raise ValidationException(
            f"TableClass must be one of {valid_table_classes}, got: {table_class}"
        )

    # --- Validate StreamSpecification ---
    if stream_spec:
        if stream_spec.get('StreamEnabled'):
            stream_view_type = stream_spec.get('StreamViewType', '')
            valid_stream_views = ('KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE', 'NEW_AND_OLD_IMAGES')
            if stream_view_type not in valid_stream_views:
                raise ValidationException(
                    f"StreamViewType must be one of {valid_stream_views}, got: {stream_view_type}"
                )

    # --- Validate LocalSecondaryIndexes (max 5) ---
    if len(lsi_list) > 5:
        raise ValidationException("Maximum of 5 local secondary indexes per table")

    # --- Validate GlobalSecondaryIndexes (max 20) ---
    if len(gsi_list) > 20:
        raise ValidationException("Maximum of 20 global secondary indexes per table")

    # --- Validate index projections ---
    valid_projection_types = ('KEYS_ONLY', 'INCLUDE', 'ALL')
    for idx_name, idx_list in [('LocalSecondaryIndexes', lsi_list), ('GlobalSecondaryIndexes', gsi_list)]:
        for i, idx in enumerate(idx_list):
            projection = idx.get('Projection', {})
            proj_type = projection.get('ProjectionType', '')
            if proj_type not in valid_projection_types:
                raise ValidationException(
                    f"{idx_name}[{i}]: ProjectionType must be one of {valid_projection_types}, got: {proj_type}"
                )

    # --- Create table in store ---
    table_desc = {
        'TableName': table_name,
        'TableStatus': 'CREATING',
        'CreationDateTime': None,  # populated by store
        'KeySchema': key_schema,
        'AttributeDefinitions': attribute_defs,
        'BillingModeSummary': {
            'BillingMode': billing_mode,
        },
        'TableClassSummary': {
            'TableClass': table_class,
        },
        'DeletionProtectionEnabled': deletion_protection,
        'ItemCount': 0,
        'TableSizeBytes': 0,
    }

    if provisioned_throughput:
        table_desc['ProvisionedThroughput'] = {
            'ReadCapacityUnits': provisioned_throughput.get('ReadCapacityUnits', 5),
            'WriteCapacityUnits': provisioned_throughput.get('WriteCapacityUnits', 5),
        }

    if stream_spec and stream_spec.get('StreamEnabled'):
        table_desc['StreamSpecification'] = stream_spec

    if sse_spec:
        table_desc['SSESpecification'] = sse_spec

    if lsi_list:
        table_desc['LocalSecondaryIndexes'] = lsi_list

    if gsi_list:
        table_desc['GlobalSecondaryIndexes'] = gsi_list

    store.create_table(table_name, table_desc, tags=tags)

    # Return the TableDescription in CREATING state
    return {
        'TableDescription': table_desc,
    }
