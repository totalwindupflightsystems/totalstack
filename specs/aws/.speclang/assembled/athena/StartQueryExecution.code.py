# spec:trace: aws/athena/StartQueryExecution.spec.py.md#implementation
# spec:id: @specs/aws/athena/startqueryexecution
# spec:generated: DO NOT EDIT — edit the spec instead

def start_query_execution(store: 'AthenaStore', request: dict) -> dict:
    """Start a new query execution."""
    query_string = request.get('QueryString')
    workgroup = request.get('WorkGroup', 'primary')
    if not query_string:
        raise InvalidRequestException('QueryString is required')

    import uuid, time
    exec_id = str(uuid.uuid4())
    qe = {
        'QueryExecutionId': exec_id,
        'Query': query_string,
        'StatementType': 'DML',
        'WorkGroup': workgroup,
        'Status': {'State': 'RUNNING', 'SubmissionDateTime': time.time()},
        'ResultConfiguration': request.get('ResultConfiguration', {}),
        'QueryExecutionContext': request.get('QueryExecutionContext', {}),
    }
    if 'ClientRequestToken' in request:
        qe['ClientRequestToken'] = request['ClientRequestToken']

    store.query_executions[exec_id] = qe

    # Simulate success for emulation
    qe['Status'] = {'State': 'SUCCEEDED', 'SubmissionDateTime': time.time(),
                     'CompletionDateTime': time.time() + 0.1}

    return {'QueryExecutionId': exec_id}

