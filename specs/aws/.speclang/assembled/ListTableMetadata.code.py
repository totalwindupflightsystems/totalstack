
def list_table_metadata(store: 'AthenaStore', request: dict) -> dict:
    """List tables in a database."""
    catalog = request.get('CatalogName', 'AwsDataCatalog')
    db_name = request.get('DatabaseName')
    if not db_name:
        raise InvalidRequestException('DatabaseName is required')
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    tables = sorted([dict(v) for (c, d, _), v in store.table_metadata.items()
                     if c == catalog and d == db_name],
                    key=lambda t: t.get('Name', ''))
    start = int(next_token) if next_token else 0
    page = tables[start:start + max_results]
    result = {'TableMetadataList': page}
    if start + max_results < len(tables):
        result['NextToken'] = str(start + max_results)
    return result
