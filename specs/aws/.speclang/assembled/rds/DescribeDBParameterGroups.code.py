def handler(store, request: dict) -> dict:
    """DescribeDBParameterGroups handler."""
    result = store.describe_db_parameter_groups(
        db_parameter_group_name=request.get("DBParameterGroupName"))
    if isinstance(result, list):
        return {"DBParameterGroups": result}
    return {"DBParameterGroups": [result]}
