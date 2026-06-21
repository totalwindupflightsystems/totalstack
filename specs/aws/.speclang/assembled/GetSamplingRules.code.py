// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetSamplingRules.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_sampling_rules(store, request):
    next_token = request.get('NextToken', '')
    all_rules = list(store.sampling_rules.values())
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_rules[start:start + page_size]
    records = []
    for r in page:
        rec = {'SamplingRule': r, 'CreatedAt': '2024-01-01T00:00:00Z', 'ModifiedAt': '2024-01-01T00:00:00Z'}
        records.append(rec)
    resp = {'SamplingRuleRecords': records}
    if start + page_size < len(all_rules):
        resp['NextToken'] = str(start + page_size)
    return resp