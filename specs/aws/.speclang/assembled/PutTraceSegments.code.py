
def put_trace_segments(store, request):
    docs = request.get('TraceSegmentDocuments', [])
    if not docs:
        raise InvalidRequestException('TraceSegmentDocuments is required')
    unprocessed = []
    import json
    for i, doc_str in enumerate(docs):
        try:
            doc = json.loads(doc_str)
            trace_id = doc.get('trace_id', f'auto-{i}')
            segments = store.traces.get(trace_id, {}).get('Segments', [])
            segments.append(doc_str)
            store.traces[trace_id] = {
                'Id': trace_id,
                'Duration': doc.get('end_time', 0) - doc.get('start_time', 0),
                'Segments': segments,
                'ServiceName': doc.get('name', 'unknown'),
                'Http': doc.get('http', {})
            }
        except Exception:
            unprocessed.append({'Id': str(i), 'ErrorCode': 'InvalidSegment', 'Message': 'Invalid JSON'})
    return {'UnprocessedTraceSegments': unprocessed}
