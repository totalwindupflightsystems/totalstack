// spec:trace spec=/home/kara/totalstack/specs/aws/athena/ListQueryExecutions.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def list_query_executions(store: 'AthenaStore', request: dict) -> dict:
    """List query executions."""
    workgroup = request.get('WorkGroup')
    max_results = request.get('MaxResults', 50)
    next_token = request.get('NextToken')

    ids = sorted(store.query_executions.keys(),
                 key=lambda x: store.query_executions[x]['Status'].get('SubmissionDateTime', 0),
                 reverse=True)
    if workgroup:
        ids = [i for i in ids if store.query_executions[i].get('WorkGroup') == workgroup]

    start = int(next_token) if next_token else 0
    page = ids[start:start + max_results]
    result = {'QueryExecutionIds': page}
    if start + max_results < len(ids):
        result['NextToken'] = str(start + max_results)
    return result