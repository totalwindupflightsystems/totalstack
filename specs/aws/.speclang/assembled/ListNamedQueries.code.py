
def list_named_queries(store: 'AthenaStore', request: dict) -> dict:
    """List named queries in a workgroup."""
    workgroup = request.get('WorkGroup', 'primary')
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    ids = [qid for qid, q in store.named_queries.items()
           if q.get('WorkGroup') == workgroup]
    ids.sort()
    start = int(next_token) if next_token else 0
    page = ids[start:start + max_results]
    result = {'NamedQueryIds': page}
    if start + max_results < len(ids):
        result['NextToken'] = str(start + max_results)
    return result
