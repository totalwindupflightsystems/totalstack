def handler(store, request: dict):
    return store.modify_parameter_group(request["DBClusterParameterGroupName"], request["Parameters"])
