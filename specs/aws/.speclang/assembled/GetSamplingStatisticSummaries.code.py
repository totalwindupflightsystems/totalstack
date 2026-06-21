// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetSamplingStatisticSummaries.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_sampling_statistic_summaries(store, request):
    next_token = request.get('NextToken', '')
    all_rules = list(store.sampling_rules.values())
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_rules[start:start + page_size]
    summaries = [{'RuleName': r['RuleName'], 'Timestamp': '2024-01-01T00:00:00Z',
                  'RequestCount': 0, 'BorrowCount': 0, 'SampledCount': 0} for r in page]
    resp = {'SamplingStatisticSummaries': summaries}
    if start + page_size < len(all_rules):
        resp['NextToken'] = str(start + page_size)
    return resp