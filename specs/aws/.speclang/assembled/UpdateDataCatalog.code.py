// spec:trace spec=/home/kara/totalstack/specs/aws/athena/UpdateDataCatalog.spec.py.md#input
// spec:generated DO NOT EDIT — edit the spec instead

def update_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Update an Athena data catalog."""
    name = request.get('Name')
    catalog_type = request.get('Type')
    if not name:
        raise InvalidRequestException('Name is required')
    if not catalog_type:
        raise InvalidRequestException('Type is required')
    if name not in store.data_catalogs:
        raise ResourceNotFoundException(f'Data catalog {name} not found')

    catalog = store.data_catalogs[name]
    catalog['Type'] = catalog_type
    if 'Description' in request:
        catalog['Description'] = request['Description']
    if 'Parameters' in request:
        catalog['Parameters'] = request['Parameters']

    return {'DataCatalog': dict(catalog)}