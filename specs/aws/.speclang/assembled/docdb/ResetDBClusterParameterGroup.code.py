def handler(store, request: dict):
    return store.reset_parameter_group(request["DBClusterParameterGroupName"], request.get("Parameters"))
