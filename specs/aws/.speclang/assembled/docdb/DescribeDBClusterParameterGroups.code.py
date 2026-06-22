def handler(store, request: dict):
    return store.describe_parameter_groups(request.get("DBClusterParameterGroupName"), **{k: v for k, v in request.items() if k != "DBClusterParameterGroupName"})
