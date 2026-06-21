# spec:trace: aws/athena/DeleteNamedQuery.spec.py.md#implementation
# spec:id: @specs/aws/athena/deletenamedquery
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_named_query(store: 'AthenaStore', request: dict) -> dict:
    """Delete a named query."""
    query_id = request.get('NamedQueryId')
    if not query_id:
        raise InvalidRequestException('NamedQueryId is required')
    if query_id not in store.named_queries:
        raise ResourceNotFoundException(f'Named query {query_id} not found')
    del store.named_queries[query_id]
    return {}

