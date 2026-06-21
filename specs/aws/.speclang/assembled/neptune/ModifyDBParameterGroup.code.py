"""ModifyDBParameterGroup handler for Neptune."""


def modify_db_parameter_group(store, request):
    """Modify parameters of a DB parameter group."""
    name = request.get('DBParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBParameterGroupName is required")

    # Verify group exists
    store.get_param_group(name)

    return {'DBParameterGroupName': name}
