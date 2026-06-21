def handler(store, request: dict) -> dict:
    return store.modify_parameter_group(request["DBParameterGroupName"], request.get("Parameters", []))
