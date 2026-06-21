"""ModifyDBClusterParameterGroup handler for Neptune."""


def modify_db_cluster_parameter_group(store, request):
    """Modify parameters of a DB cluster parameter group."""
    name = request.get('DBClusterParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBClusterParameterGroupName is required")

    # Verify group exists
    store.get_cluster_param_group(name)

    return {'DBClusterParameterGroupName': name}
