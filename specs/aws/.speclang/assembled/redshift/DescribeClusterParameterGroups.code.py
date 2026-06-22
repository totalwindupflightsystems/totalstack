def handler(store, request: dict) -> dict:
    return store.describe_cluster_parameter_groups(
        ParameterGroupName=request.get("ParameterGroupName"))
