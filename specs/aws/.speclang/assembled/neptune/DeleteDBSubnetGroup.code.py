"""DeleteDBSubnetGroup handler for Neptune."""


def delete_db_subnet_group(store, request):
    """Delete a DB subnet group."""
    name = request.get('DBSubnetGroupName', '').strip()
    if not name:
        raise InvalidParameterValueException("DBSubnetGroupName is required")

    store.delete_subnet_group(name)
    return {}
