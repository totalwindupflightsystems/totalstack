def handler(store, request: dict) -> dict:
    return store.modify_cluster_parameter_group(
        request["ParameterGroupName"],
        request["Parameters"])
