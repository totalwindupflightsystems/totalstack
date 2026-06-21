// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetGroups.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_groups(store, request):
    next_token = request.get('NextToken', '')
    all_groups = list(store.groups.values())
    page_size = 100
    start = int(next_token) if next_token else 0
    page = all_groups[start:start + page_size]
    result_groups = []
    for g in page:
        r = dict(g)
        arn = g.get('GroupARN', '')
        if arn in store.tags:
            r['Tags'] = [{'Key': k, 'Value': v} for k, v in store.tags[arn].items()]
        result_groups.append(r)
    resp = {'Groups': result_groups}
    if start + page_size < len(all_groups):
        resp['NextToken'] = str(start + page_size)
    return resp