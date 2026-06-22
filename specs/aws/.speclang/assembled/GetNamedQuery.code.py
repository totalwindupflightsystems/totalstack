
def get_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Get a named query by ID."""
    query_id = request.get('NamedQueryId')
    if not query_id:
        raise InvalidRequestException('NamedQueryId is required')
    if query_id not in store.named_queries:
        raise ResourceNotFoundException(f'Named query {query_id} not found')
    return {'NamedQuery': dict(store.named_queries[query_id])}
