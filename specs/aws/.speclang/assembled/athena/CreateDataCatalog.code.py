# spec:trace: aws/athena/CreateDataCatalog.spec.py.md#implementation
# spec:id: @specs/aws/athena/createdatacatalog
# spec:generated: DO NOT EDIT — edit the spec instead

def create_data_catalog(store: 'AthenaStore', request: dict) -> dict:
    """Create a new Athena data catalog."""
    name = request.get('Name')
    catalog_type = request.get('Type')
    if not name:
        raise InvalidRequestException('Name is required')
    if not catalog_type:
        raise InvalidRequestException('Type is required')
    if name in store.data_catalogs:
        raise InvalidRequestException(f'Data catalog {name} already exists')

    catalog = {
        'Name': name,
        'Type': catalog_type,
        'Description': request.get('Description', ''),
        'Parameters': request.get('Parameters', {}),
    }
    store.data_catalogs[name] = catalog

    # Handle tags
    tags = request.get('Tags', [])
    if tags:
        arn = f'arn:aws:athena:us-east-1:000000000000:datacatalog/{name}'
        store.tags[arn] = {t['Key']: t['Value'] for t in tags}

    return {'DataCatalog': dict(catalog)}

