
def get_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Get an Athena data catalog by name."""
    name = request.get('Name')
    if not name:
        raise InvalidRequestException('Name is required')
    if name not in store.data_catalogs:
        raise ResourceNotFoundException(f'Data catalog {name} not found')
    return {'DataCatalog': dict(store.data_catalogs[name])}
