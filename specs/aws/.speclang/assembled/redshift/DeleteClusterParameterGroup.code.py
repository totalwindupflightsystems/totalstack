def handler(store, request: dict) -> dict:
    store.delete_cluster_parameter_group(request["ParameterGroupName"])
    return {}
