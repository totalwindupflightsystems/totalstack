"""DescribeDBInstances handler for Neptune."""


def describe_db_instances(store, request):
    """Describe Neptune DB instances."""
    identifier = request.get('DBInstanceIdentifier', '').strip() or None
    max_records = request.get('MaxRecords', 100)

    instances = store.list_instances(
        db_instance_identifier=identifier,
        max_records=max_records,
    )
    return {'DBInstances': [i.to_dict() for i in instances]}
