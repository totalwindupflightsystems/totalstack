
def get_time_series_service_statistics(store, request):
    start_time = request.get('StartTime')
    end_time = request.get('EndTime')
    if not start_time or not end_time:
        raise InvalidRequestException('StartTime and EndTime are required')
    group_name = request.get('GroupName', '')
    group_arn = request.get('GroupARN', '')
    entity_selector = request.get('EntitySelectorExpression', '')
    period = request.get('Period', 300)
    forecast_end = request.get('ForecastStatistics', False)
    next_token = request.get('NextToken', '')
    stats = []
    seen = set()
    for trace in store.traces.values():
        svc = trace.get('ServiceName', 'unknown')
        if svc not in seen:
            seen.add(svc)
            stats.append({'Timestamp': end_time, 'EdgeSummaryStatistics': {},
                         'ServiceSummaryStatistics': {'OkCount': 1}, 'FaultSummaryStatistics': {},
                         'ServiceName': svc, 'ResponseTimeHistogram': []})
    resp = {'TimeSeriesServiceStatistics': stats, 'ContainsOldGroupVersions': False}
    if next_token:
        resp['NextToken'] = next_token
    return resp
