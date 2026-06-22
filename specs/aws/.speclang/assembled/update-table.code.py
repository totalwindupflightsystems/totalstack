
# spec:trace: specs/aws/dynamodb/dynamodb.spec.plan.md#operation-inventory-57-total
# spec:id: @specs/aws/dynamodb/update-table
# spec:implements: @kind:operation UpdateTable

def update_table(store: DynamoDBStore, request: dict) -> dict:
    """
    Modifies table settings: throughput, GSIs, streams, SSE, table class,
    deletion protection, on-demand throughput, and warm throughput.

    AWS API reference:
    https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateTable.html

    Required fields: TableName
    Output: {TableDescription: {...}}
    Errors: ResourceInUseException, ResourceNotFoundException, LimitExceededException,
            InternalServerError
    """
    # --- Validate required fields ---
    if 'TableName' not in request or not request['TableName']:
        raise ValidationException("TableName is required")

    table_name = request['TableName']
    billing_mode = request.get('BillingMode')
    provisioned_throughput = request.get('ProvisionedThroughput')
    gsi_updates = request.get('GlobalSecondaryIndexUpdates', [])
    stream_spec = request.get('StreamSpecification')
    sse_spec = request.get('SSESpecification')
    replica_updates = request.get('ReplicaUpdates', [])
    table_class = request.get('TableClass')
    deletion_protection = request.get('DeletionProtectionEnabled')
    multi_region_consistency = request.get('MultiRegionConsistency')
    global_witness_updates = request.get('GlobalTableWitnessUpdates', [])
    on_demand_throughput = request.get('OnDemandThroughput')
    warm_throughput = request.get('WarmThroughput')

    # --- Check table exists ---
    if not store.table_exists(table_name):
        raise ResourceNotFoundException(f"Table {table_name} not found")

    table_desc = store.get_table_description(table_name)
    status = table_desc.get('TableStatus', '')

    # --- Check table state ---
    if status != 'ACTIVE':
        raise ResourceInUseException(
            f"Table {table_name} is in {status} state, must be ACTIVE to update"
        )

    # --- Validate BillingMode if provided ---
    if billing_mode:
        valid_billing_modes = ('PAY_PER_REQUEST', 'PROVISIONED')
        if billing_mode not in valid_billing_modes:
            raise ValidationException(
                f"BillingMode must be one of {valid_billing_modes}, got: {billing_mode}"
            )

    # --- Validate TableClass if provided ---
    if table_class:
        valid_table_classes = ('STANDARD', 'STANDARD_INFREQUENT_ACCESS')
        if table_class not in valid_table_classes:
            raise ValidationException(
                f"TableClass must be one of {valid_table_classes}, got: {table_class}"
            )

    # --- Validate StreamSpecification ---
    if stream_spec:
        current_stream = table_desc.get('StreamSpecification')
        stream_enabled_now = current_stream.get('StreamEnabled', False) if current_stream else False
        stream_enabled_new = stream_spec.get('StreamEnabled', False)

        # Cannot enable stream on a table that already has one
        if stream_enabled_new and stream_enabled_now:
            raise ValidationException(
                "Cannot enable stream on a table that already has a stream enabled"
            )
        # Cannot disable stream on a table that doesn't have one
        if not stream_enabled_new and not stream_enabled_now:
            raise ValidationException(
                "Cannot disable stream on a table that doesn't have a stream enabled"
            )

        if stream_enabled_new:
            stream_view_type = stream_spec.get('StreamViewType', '')
            valid_stream_views = ('KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE', 'NEW_AND_OLD_IMAGES')
            if stream_view_type not in valid_stream_views:
                raise ValidationException(
                    f"StreamViewType must be one of {valid_stream_views}, got: {stream_view_type}"
                )

    # --- Validate GSI updates: only one create or delete per operation ---
    create_count = sum(1 for u in gsi_updates if 'Create' in u)
    delete_count = sum(1 for u in gsi_updates if 'Delete' in u)
    if create_count > 1 or delete_count > 1:
        raise ValidationException(
            "Only one global secondary index can be created or deleted per UpdateTable operation"
        )

    # --- Validate MultiRegionConsistency if provided ---
    if multi_region_consistency:
        valid_consistency_modes = ('EVENTUAL', 'STRONG')
        if multi_region_consistency not in valid_consistency_modes:
            raise ValidationException(
                f"MultiRegionConsistency must be one of {valid_consistency_modes}, "
                f"got: {multi_region_consistency}"
            )

    # --- Apply updates ---
    table_desc['TableStatus'] = 'UPDATING'

    if billing_mode:
        if 'BillingModeSummary' not in table_desc:
            table_desc['BillingModeSummary'] = {}
        table_desc['BillingModeSummary']['BillingMode'] = billing_mode

    if provisioned_throughput:
        table_desc['ProvisionedThroughput'] = {
            'ReadCapacityUnits': provisioned_throughput.get('ReadCapacityUnits', 5),
            'WriteCapacityUnits': provisioned_throughput.get('WriteCapacityUnits', 5),
        }

    if stream_spec:
        table_desc['StreamSpecification'] = stream_spec

    if sse_spec:
        table_desc['SSESpecification'] = sse_spec

    if table_class:
        table_desc['TableClassSummary'] = {'TableClass': table_class}

    if deletion_protection is not None:
        table_desc['DeletionProtectionEnabled'] = deletion_protection

    if on_demand_throughput:
        table_desc['OnDemandThroughput'] = on_demand_throughput

    if warm_throughput:
        table_desc['WarmThroughput'] = warm_throughput

    # Apply GSI updates
    if gsi_updates:
        existing_gsis = table_desc.get('GlobalSecondaryIndexes', [])
        for update in gsi_updates:
            if 'Create' in update:
                existing_gsis.append(update['Create'])
            elif 'Delete' in update:
                idx_name = update['Delete']['IndexName']
                existing_gsis = [g for g in existing_gsis if g.get('IndexName') != idx_name]
            elif 'Update' in update:
                idx_name = update['Update']['IndexName']
                for gsi in existing_gsis:
                    if gsi.get('IndexName') == idx_name:
                        gsi['ProvisionedThroughput'] = update['Update']['ProvisionedThroughput']
        table_desc['GlobalSecondaryIndexes'] = existing_gsis

    store.update_table(table_name, table_desc)

    return {
        'TableDescription': table_desc,
    }
