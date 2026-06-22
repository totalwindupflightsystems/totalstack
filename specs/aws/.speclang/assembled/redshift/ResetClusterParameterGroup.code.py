def handler(store, request: dict) -> dict:
    return store.reset_cluster_parameter_group(
        request["ParameterGroupName"],
        Parameters=request.get("Parameters"),
        ResetAllParameters=request.get("ResetAllParameters"))
