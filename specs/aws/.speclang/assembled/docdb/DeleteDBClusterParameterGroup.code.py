def handler(store, request: dict):
    return store.delete_parameter_group(request["DBClusterParameterGroupName"])
