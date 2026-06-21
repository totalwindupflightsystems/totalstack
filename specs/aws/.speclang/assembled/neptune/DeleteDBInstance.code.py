"""DeleteDBInstance handler for Neptune."""


def delete_db_instance(store, request):
    """Delete a Neptune DB instance."""
    identifier = request.get('DBInstanceIdentifier', '').strip()
    if not identifier:
        raise InvalidParameterValueException("DBInstanceIdentifier is required")

    skip_final = request.get('SkipFinalSnapshot', False)
    instance = store.delete_instance(identifier, skip_final_snapshot=skip_final)
    return {'DBInstance': instance.to_dict()}
