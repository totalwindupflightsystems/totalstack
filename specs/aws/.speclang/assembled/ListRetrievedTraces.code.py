// spec:trace spec=/home/kara/totalstack/specs/aws/xray/ListRetrievedTraces.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def list_retrieved_traces(store, request):
    token = request.get('RetrievalToken', '')
    if not token:
        raise InvalidRequestException('RetrievalToken is required')
    retrieval = store.trace_retrievals.get(token)
    if not retrieval:
        raise InvalidRequestException(f'Retrieval token not found')
    next_token = request.get('NextToken', '')
    all_tids = retrieval['TraceIds']
    retrieval_format = request.get('TraceFormat', 'XRAY_SEGMENT_DOCUMENT')
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_tids[start:start + page_size]
    traces = []
    for tid in page:
        trace = store.traces.get(tid)
        if trace:
            traces.append(trace)
    resp = {'TraceFormat': retrieval_format, 'RetrievedTraces': traces, 'RetrievalStatus': 'COMPLETE', 'TraceCount': len(page)}
    if start + page_size < len(all_tids):
        resp['NextToken'] = str(start + page_size)
    return resp