"""CreateDBParameterGroup handler for Neptune."""


def create_db_parameter_group(store, request):
    """Create a new DB parameter group."""
    name = request.get('DBParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBParameterGroupName is required")

    family = request.get('DBParameterGroupFamily', '').strip()
    if not family:
        raise InvalidParameterValueException("DBParameterGroupFamily is required")

    description = request.get('Description', '').strip()
    if not description:
        raise InvalidParameterValueException("Description is required")

    pg = store.create_param_group(
        name, family, description,
        tags=request.get('Tags', []),
    )
    return {'DBParameterGroup': pg.to_dict()}
