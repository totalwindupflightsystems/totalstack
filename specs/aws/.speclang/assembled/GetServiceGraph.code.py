// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetServiceGraph.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_service_graph(store, request):
    start_time = request.get('StartTime')
    end_time = request.get('EndTime')
    if not start_time or not end_time:
        raise InvalidRequestException('StartTime and EndTime are required')
    group_name = request.get('GroupName', '')
    group_arn = request.get('GroupARN', '')
    next_token = request.get('NextToken', '')
    services = []
    seen = set()
    for trace in store.traces.values():
        svc_name = trace.get('ServiceName', 'unknown')
        if svc_name not in seen:
            seen.add(svc_name)
            services.append({'ReferenceId': len(seen), 'Name': svc_name,
                           'Names': [svc_name], 'Type': 'client',
                           'StartTime': start_time, 'EndTime': end_time})
    resp = {'Services': services, 'StartTime': start_time, 'EndTime': end_time}
    if next_token:
        resp['NextToken'] = next_token
    return resp