def handler(store, request: dict) -> dict:
    """DeleteDBParameterGroup handler."""
    store.delete_db_parameter_group(
        db_parameter_group_name=request["DBParameterGroupName"])
    return {}
