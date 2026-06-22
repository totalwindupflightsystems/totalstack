
def get_insight_events(store, request):
    insight_id = request.get('InsightId', '')
    if not insight_id:
        raise InvalidRequestException('InsightId is required')
    insight = store.insights.get(insight_id)
    if not insight:
        raise InvalidRequestException(f'Insight not found')
    next_token = request.get('NextToken', '')
    max_results = request.get('MaxResults', 50)
    events = insight.get('Events', [])
    page = events[:max_results]
    resp = {'InsightEvents': page}
    if len(page) < len(events):
        resp['NextToken'] = str(len(page))
    return resp
