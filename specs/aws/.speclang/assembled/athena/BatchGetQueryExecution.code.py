# spec:trace: aws/athena/BatchGetQueryExecution.spec.py.md#implementation
# spec:id: @specs/aws/athena/batchgetqueryexecution
# spec:generated: DO NOT EDIT — edit the spec instead

def batch_get_query_execution(store: 'AthenaStore', request: dict) -> dict:
    """Batch get query executions."""
    ids = request.get('QueryExecutionIds', [])
    queries, unprocessed = [], []
    for eid in ids:
        if eid in store.query_executions:
            queries.append(dict(store.query_executions[eid]))
        else:
            unprocessed.append({'QueryExecutionId': eid, 'ErrorCode': 'ResourceNotFound'})
    result = {'QueryExecutions': queries}
    if unprocessed:
        result['UnprocessedQueryExecutionIds'] = unprocessed
    return result

