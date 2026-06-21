// spec:trace spec=/home/kara/totalstack/specs/aws/athena/UpdateNamedQuery.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def update_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Update a named query."""
    query_id = request.get('NamedQueryId')
    if not query_id:
        raise InvalidRequestException('NamedQueryId is required')
    if query_id not in store.named_queries:
        raise ResourceNotFoundException(f'Named query {query_id} not found')
    nq = store.named_queries[query_id]
    if 'Name' in request:
        nq['Name'] = request['Name']
    if 'Description' in request:
        nq['Description'] = request['Description']
    if 'QueryString' in request:
        nq['QueryString'] = request['QueryString']
    return {}