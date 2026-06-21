// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetIndexingRules.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_indexing_rules(store, request):
    next_token = request.get('NextToken', '')
    all_rules = list(store.indexing_rules.values())
    resp = {'IndexingRules': all_rules}
    if next_token:
        resp['NextToken'] = next_token
    return resp