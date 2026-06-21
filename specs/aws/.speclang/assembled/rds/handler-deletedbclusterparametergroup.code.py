def handler(store, request: dict) -> dict:
    return store.delete_cluster_parameter_group(request["DBClusterParameterGroupName"])
