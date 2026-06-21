"""RebootDBInstance handler for Neptune."""


def reboot_db_instance(store, request):
    """Reboot a Neptune DB instance."""
    identifier = request.get('DBInstanceIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBInstanceIdentifier is required")

    instance = store.get_instance(identifier)
    instance.status = 'rebooting'
    return {'DBInstance': instance.to_dict()}
