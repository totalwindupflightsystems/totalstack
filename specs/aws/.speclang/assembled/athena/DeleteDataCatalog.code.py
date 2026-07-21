# spec:trace: aws/athena/DeleteDataCatalog.spec.py.md#implementation
# spec:id: @specs/aws/athena/deletedatacatalog
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Delete an Athena data catalog."""
    name = request.get('Name')
    if not name:
        raise InvalidRequestException('Name is required')
    if name not in store.data_catalogs:
        raise ResourceNotFoundException(f'Data catalog {name} not found')
    catalog = store.data_catalogs[name]
    del store.data_catalogs[name]
    return {'DataCatalog': dict(catalog)}

