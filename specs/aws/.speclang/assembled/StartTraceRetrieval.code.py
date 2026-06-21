// spec:trace spec=/home/kara/totalstack/specs/aws/xray/StartTraceRetrieval.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def start_trace_retrieval(store, request):
    trace_ids = request.get('TraceIds', [])
    start_time = request.get('StartTime')
    end_time = request.get('EndTime')
    if not trace_ids or not start_time or not end_time:
        raise InvalidRequestException('TraceIds, StartTime, and EndTime are required')
    import uuid
    token = str(uuid.uuid4())
    store.trace_retrievals[token] = {
        'RetrievalToken': token,
        'TraceIds': trace_ids,
        'StartTime': start_time,
        'EndTime': end_time,
        'Status': 'COMPLETE',
        'RetrievalStartTime': start_time,
        'RetrievalEndTime': end_time,
        'TraceCount': len([t for t in trace_ids if t in store.traces]),
        'TraceFormat': 'XRAY_SEGMENT_DOCUMENT',
    }
    return {'RetrievalToken': token, 'TraceFormat': 'XRAY_SEGMENT_DOCUMENT'}