
def get_insight_impact_graph(store, request):
    insight_id = request.get('InsightId', '')
    start_time = request.get('StartTime')
    end_time = request.get('EndTime')
    if not insight_id:
        raise InvalidRequestException('InsightId is required')
    if not start_time or not end_time:
        raise InvalidRequestException('StartTime and EndTime are required')
    insight = store.insights.get(insight_id)
    if not insight:
        raise InvalidRequestException(f'Insight not found')
    next_token = request.get('NextToken', '')
    services = insight.get('ImpactServices', [])
    resp = {'InsightId': insight_id, 'StartTime': start_time, 'EndTime': end_time,
            'ServiceGraph': services, 'NextToken': next_token or ''}
    return resp
