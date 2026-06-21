// spec:trace spec=/home/kara/totalstack/specs/aws/xray/ListResourcePolicies.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def list_resource_policies(store, request):
    next_token = request.get('NextToken', '')
    all_policies = list(store.resource_policies.values())
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_policies[start:start + page_size]
    resp = {'ResourcePolicies': page}
    if start + page_size < len(all_policies):
        resp['NextToken'] = str(start + page_size)
    return resp