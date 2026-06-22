
def get_trace_summaries(store, request):
    start_time = request.get('StartTime')
    end_time = request.get('EndTime')
    if not start_time or not end_time:
        raise InvalidRequestException('StartTime and EndTime are required')
    next_token = request.get('NextToken', '')
    filter_expr = request.get('FilterExpression', '')
    sampling = request.get('Sampling', False)
    time_range_type = request.get('TimeRangeType', 'TraceId')
    all_trace_ids = list(store.traces.keys())
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_trace_ids[start:start + page_size]
    summaries = [{'Id': tid, 'Duration': store.traces[tid].get('Duration', 0),
                  'Http': store.traces[tid].get('Http', {}),
                  'ServiceIds': [], 'HasError': False,
                  'HasFault': False, 'HasThrottle': False,
                  'IsPartial': False, 'HasUser': True,
                  'Revision': 1, 'EntryPoint': {'Name': 'test', 'URL': '/', 'Type': 'HTTP'},
                  'ResponseTime': store.traces[tid].get('Duration', 0)} for tid in page]
    resp = {'TraceSummaries': summaries, 'ApproximateTime': end_time, 'TracesProcessedCount': len(summaries)}
    if start + page_size < len(all_trace_ids):
        resp['NextToken'] = str(start + page_size)
    return resp
