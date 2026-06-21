"""DescribeDBParameterGroups handler for Neptune."""


def describe_db_parameter_groups(store, request):
    """Describe DB parameter groups."""
    name = request.get('DBParameterGroupName', '').strip() or None
    max_records = request.get('MaxRecords', 100)

    groups = store.list_param_groups(name=name, max_records=max_records)
    return {'DBParameterGroups': [g.to_dict() for g in groups]}
