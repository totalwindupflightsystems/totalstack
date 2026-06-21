def handler(store, request: dict) -> dict:
    """DescribeDBInstances handler."""
    result = store.describe_db_instances(
        db_instance_identifier=request.get("DBInstanceIdentifier"))
    if isinstance(result, list):
        return {"DBInstances": result}
    return {"DBInstances": [result]}
