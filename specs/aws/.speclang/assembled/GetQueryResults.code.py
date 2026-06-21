// spec:trace spec=/home/kara/totalstack/specs/aws/athena/GetQueryResults.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_query_results(store: 'AthenaStore', request: dict) -> dict:
    """Get query results."""
    exec_id = request.get('QueryExecutionId')
    if not exec_id:
        raise InvalidRequestException('QueryExecutionId is required')
    if exec_id not in store.query_executions:
        raise ResourceNotFoundException(f'Query execution {exec_id} not found')
    qe = store.query_executions[exec_id]
    if qe['Status']['State'] != 'SUCCEEDED':
        raise InvalidRequestException('Query has not succeeded; current state: ' + qe['Status']['State'])

    max_results = request.get('MaxResults', 1000)
    next_token = request.get('NextToken')
    start = int(next_token) if next_token else 0

    # Stored results or empty
    results = qe.get('_results', [])
    page = results[start:start + max_results]
    result = {
        'ResultSet': {
            'Rows': page,
            'ResultSetMetadata': {'ColumnInfo': qe.get('_column_info', [])},
        },
        'UpdateCount': len(page),
    }
    if start + max_results < len(results):
        result['NextToken'] = str(start + max_results)
    return result