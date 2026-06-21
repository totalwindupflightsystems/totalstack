"""DeleteDBClusterParameterGroup handler for Neptune."""


def delete_db_cluster_parameter_group(store, request):
    """Delete a DB cluster parameter group."""
    name = request.get('DBClusterParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBClusterParameterGroupName is required")

    store.delete_cluster_param_group(name)
    return {}
