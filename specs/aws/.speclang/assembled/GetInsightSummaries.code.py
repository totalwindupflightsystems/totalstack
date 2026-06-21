// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetInsightSummaries.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_insight_summaries(store, request):
    start_time = request.get('StartTime')
    end_time = request.get('EndTime')
    if not start_time or not end_time:
        raise InvalidRequestException('StartTime and EndTime are required')
    next_token = request.get('NextToken', '')
    states = request.get('States', [])
    group_arn = request.get('GroupARN', '')
    all_insights = list(store.insights.values())
    if states:
        all_insights = [i for i in all_insights if i.get('State') in states]
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_insights[start:start + page_size]
    summaries = [{'InsightId': i.get('InsightId', ''), 'GroupARN': i.get('GroupARN', ''),
                  'GroupName': i.get('GroupName', ''), 'RootCauseServiceId': {},
                  'Categories': i.get('Categories', []), 'State': i.get('State', 'ACTIVE'),
                  'StartTime': start_time, 'EndTime': end_time,
                  'Summary': i.get('Summary', ''), 'ClientRequestImpactStatistics': {},
                  'TopAnomalousServices': []} for i in page]
    resp = {'InsightSummaries': summaries}
    if start + page_size < len(all_insights):
        resp['NextToken'] = str(start + page_size)
    return resp