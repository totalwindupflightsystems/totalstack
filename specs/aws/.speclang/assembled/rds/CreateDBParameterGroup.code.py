def handler(store, request: dict) -> dict:
    """CreateDBParameterGroup handler."""
    return store.create_db_parameter_group(
        db_parameter_group_name=request["DBParameterGroupName"],
        db_parameter_group_family=request["DBParameterGroupFamily"],
        description=request["Description"],
        tags=request.get("Tags"))
