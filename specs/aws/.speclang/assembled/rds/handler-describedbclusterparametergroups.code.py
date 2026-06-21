def handler(store, request: dict) -> dict:
    name = request.get("DBClusterParameterGroupName")
    return store.describe_cluster_parameter_groups(name)
