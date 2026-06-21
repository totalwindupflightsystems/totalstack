"""DescribeDBSubnetGroups handler for Neptune."""


def describe_db_subnet_groups(store, request):
    """Describe DB subnet groups."""
    name = request.get('DBSubnetGroupName', '').strip() or None
    max_records = request.get('MaxRecords', 100)

    groups = store.list_subnet_groups(name=name, max_records=max_records)
    return {'DBSubnetGroups': [g.to_dict() for g in groups]}
