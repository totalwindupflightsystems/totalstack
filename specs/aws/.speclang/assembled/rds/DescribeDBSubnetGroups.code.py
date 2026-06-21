def handler(store, request: dict) -> dict:
    """DescribeDBSubnetGroups handler."""
    result = store.describe_db_subnet_groups(
        db_subnet_group_name=request.get("DBSubnetGroupName"))
    if isinstance(result, list):
        return {"DBSubnetGroups": result}
    return {"DBSubnetGroups": [result]}
