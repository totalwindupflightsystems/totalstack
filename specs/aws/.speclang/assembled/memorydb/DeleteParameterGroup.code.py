def handler(store, request: dict) -> dict:
    return store.delete_parameter_group(request["ParameterGroupName"])

