// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetRetrievedTracesGraph.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_retrieved_traces_graph(store, request):
    token = request.get('RetrievalToken', '')
    if not token:
        raise InvalidRequestException('RetrievalToken is required')
    retrieval = store.trace_retrievals.get(token)
    if not retrieval:
        raise InvalidRequestException(f'Retrieval token not found')
    services = []
    seen = set()
    for tid in retrieval['TraceIds']:
        trace = store.traces.get(tid)
        if trace:
            svc_name = trace.get('ServiceName', 'unknown')
            if svc_name not in seen:
                seen.add(svc_name)
                services.append({'ReferenceId': len(seen), 'Name': svc_name, 'Names': [svc_name]})
    return {'Services': services, 'NextToken': request.get('NextToken', '')}