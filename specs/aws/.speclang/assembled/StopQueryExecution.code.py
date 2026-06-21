// spec:trace spec=/home/kara/totalstack/specs/aws/athena/StopQueryExecution.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def stop_query_execution(store: 'AthenaStore', request: dict) -> dict:
    """Stop a query execution."""
    exec_id = request.get('QueryExecutionId')
    if not exec_id:
        raise InvalidRequestException('QueryExecutionId is required')
    if exec_id not in store.query_executions:
        raise ResourceNotFoundException(f'Query execution {exec_id} not found')
    qe = store.query_executions[exec_id]
    import time
    qe['Status'] = {'State': 'CANCELLED', 'SubmissionDateTime': qe['Status'].get('SubmissionDateTime', time.time()),
                     'CompletionDateTime': time.time()}
    return {}