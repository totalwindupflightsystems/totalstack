"""DeleteDBParameterGroup handler for Neptune."""


def delete_db_parameter_group(store, request):
    """Delete a DB parameter group."""
    name = request.get('DBParameterGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBParameterGroupName is required")

    store.delete_param_group(name)
    return {}
