// spec:trace spec=/home/kara/totalstack/specs/aws/athena/GetTableMetadata.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_table_metadata(store: 'AthenaStore', request: dict) -> dict:
    """Get table metadata."""
    catalog = request.get('CatalogName', 'AwsDataCatalog')
    db_name = request.get('DatabaseName')
    table_name = request.get('TableName')
    if not db_name or not table_name:
        raise InvalidRequestException('DatabaseName and TableName are required')
    key = (catalog, db_name, table_name)
    if key not in store.table_metadata:
        raise ResourceNotFoundException(f'Table {table_name} not found in {catalog}.{db_name}')
    return {'TableMetadata': dict(store.table_metadata[key])}