// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetInsight.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_insight(store, request):
    insight_id = request.get('InsightId', '')
    if not insight_id:
        raise InvalidRequestException('InsightId is required')
    insight = store.insights.get(insight_id)
    if not insight:
        raise InvalidRequestException(f'Insight not found')
    return {'Insight': insight}