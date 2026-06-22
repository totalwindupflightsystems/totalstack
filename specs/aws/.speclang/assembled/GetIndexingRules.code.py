
def get_indexing_rules(store, request):
    next_token = request.get('NextToken', '')
    all_rules = list(store.indexing_rules.values())
    resp = {'IndexingRules': all_rules}
    if next_token:
        resp['NextToken'] = next_token
    return resp
