def handler(store, request: dict):
    return store.create_parameter_group(request["DBClusterParameterGroupName"], request["DBParameterGroupFamily"], request["Description"])
