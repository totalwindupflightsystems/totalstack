def handler(store, request: dict) -> dict:
    """ModifyDBParameterGroup handler."""
    return store.modify_db_parameter_group(
        db_parameter_group_name=request["DBParameterGroupName"],
        parameters=request["Parameters"])
