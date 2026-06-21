"""CreateDBClusterParameterGroup handler for Neptune."""


def create_db_cluster_parameter_group(store, request):
    """Create a new DB cluster parameter group."""
    name = request.get('DBClusterParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBClusterParameterGroupName is required")

    family = request.get('DBParameterGroupFamily', '').strip()
    if not family:
        raise InvalidParameterValueException("DBParameterGroupFamily is required")

    description = request.get('Description', '').strip()
    if not description:
        raise InvalidParameterValueException("Description is required")

    pg = store.create_cluster_param_group(
        name, family, description,
        tags=request.get('Tags', []),
    )
    return {'DBClusterParameterGroup': pg.to_dict()}
