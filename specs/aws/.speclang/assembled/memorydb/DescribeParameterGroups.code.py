def handler(store, request: dict) -> dict:
    pn = request.get("ParameterGroupName")
    return store.describe_parameter_groups(ParameterGroupName=pn)

