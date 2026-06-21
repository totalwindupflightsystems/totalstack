def handler(store, request: dict) -> dict:
    name = request.get("DBParameterGroupName")
    return store.describe_parameter_groups(name)
