def handler(store, request: dict) -> dict:
    """CreateDBClusterParameterGroup handler."""
    return store.create_db_cluster_parameter_group(
        db_cluster_parameter_group_name=request["DBClusterParameterGroupName"],
        db_parameter_group_family=request["DBParameterGroupFamily"],
        description=request["Description"],
        tags=request.get("Tags"))
