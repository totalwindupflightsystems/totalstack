def handler(store, request: dict) -> dict:
    return store.create_cluster_parameter_group(
        request["DBClusterParameterGroupName"],
        request["DBParameterGroupFamily"],
        request["Description"],
    )
