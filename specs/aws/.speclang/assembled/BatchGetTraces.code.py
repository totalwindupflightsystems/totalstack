// spec:trace spec=/home/kara/totalstack/specs/aws/xray/BatchGetTraces.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def batch_get_traces(store, request):
    trace_ids = request.get('TraceIds', [])
    if not trace_ids:
        raise InvalidRequestException('TraceIds is required')
    next_token = request.get('NextToken', '')
    traces = []
    unprocessed = []
    for tid in trace_ids:
        trace = store.traces.get(tid)
        if trace:
            traces.append(trace)
        else:
            unprocessed.append(tid)
    resp = {'Traces': traces, 'UnprocessedTraceIds': unprocessed}
    if next_token:
        resp['NextToken'] = next_token
    return resp