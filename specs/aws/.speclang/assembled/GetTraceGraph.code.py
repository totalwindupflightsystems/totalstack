// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetTraceGraph.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_trace_graph(store, request):
    trace_ids = request.get('TraceIds', [])
    if not trace_ids:
        raise InvalidRequestException('TraceIds is required')
    next_token = request.get('NextToken', '')
    services = []
    seen = set()
    for tid in trace_ids:
        trace = store.traces.get(tid)
        if trace:
            svc_name = trace.get('ServiceName', 'unknown')
            if svc_name not in seen:
                seen.add(svc_name)
                services.append({'ReferenceId': len(seen), 'Name': svc_name, 'Names': [svc_name], 'Type': 'client', 'Root': True})
    resp = {'Services': services}
    if next_token:
        resp['NextToken'] = next_token
    return resp