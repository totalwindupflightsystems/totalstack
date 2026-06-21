def handler(store, request: dict) -> dict:
    """DeleteDBClusterParameterGroup handler."""
    store.delete_db_cluster_parameter_group(
        db_cluster_parameter_group_name=request["DBClusterParameterGroupName"])
    return {}
