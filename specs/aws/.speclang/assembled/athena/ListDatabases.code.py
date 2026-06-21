# spec:trace: aws/athena/ListDatabases.spec.py.md#implementation
# spec:id: @specs/aws/athena/listdatabases
# spec:generated: DO NOT EDIT — edit the spec instead

def list_databases(store: 'AthenaStore', request: dict) -> dict:
    """List databases in a catalog."""
    catalog = request.get('CatalogName', 'AwsDataCatalog')
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    dbs = sorted([dict(v) for (c, _), v in store.databases.items() if c == catalog],
                 key=lambda d: d.get('Name', ''))
    start = int(next_token) if next_token else 0
    page = dbs[start:start + max_results]
    result = {'DatabaseList': page}
    if start + max_results < len(dbs):
        result['NextToken'] = str(start + max_results)
    return result

