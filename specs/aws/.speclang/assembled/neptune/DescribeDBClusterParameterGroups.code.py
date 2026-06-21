"""DescribeDBClusterParameterGroups handler for Neptune."""


def describe_db_cluster_parameter_groups(store, request):
    """Describe DB cluster parameter groups."""
    name = request.get('DBClusterParameterGroupName', '').strip() or None
    max_records = request.get('MaxRecords', 100)

    groups = store.list_cluster_param_groups(name=name, max_records=max_records)
    return {'DBClusterParameterGroups': [g.to_dict() for g in groups]}
