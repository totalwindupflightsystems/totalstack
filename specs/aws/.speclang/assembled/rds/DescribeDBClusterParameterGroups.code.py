def handler(store, request: dict) -> dict:
    """DescribeDBClusterParameterGroups handler."""
    result = store.describe_db_cluster_parameter_groups(
        db_cluster_parameter_group_name=request.get("DBClusterParameterGroupName"))
    if isinstance(result, list):
        return {"DBClusterParameterGroups": result}
    return {"DBClusterParameterGroups": [result]}
