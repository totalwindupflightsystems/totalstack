// spec:trace spec=/home/kara/totalstack/specs/aws/xray/UpdateGroup.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def update_group(store, request):
    group_name = request.get('GroupName', '')
    group_arn = request.get('GroupARN', '')
    if not group_name and not group_arn:
        raise InvalidRequestException('GroupName or GroupARN is required')
    groups = store.groups
    if group_arn:
        group = next((g for g in groups.values() if g.get('GroupARN') == group_arn), None)
        if group:
            group_name = group['GroupName']
    else:
        group = groups.get(group_name)
    if not group:
        raise InvalidRequestException(f'Group not found')
    if 'FilterExpression' in request:
        group['FilterExpression'] = request['FilterExpression']
    if 'InsightsConfiguration' in request:
        group['InsightsConfiguration'] = request['InsightsConfiguration']
    groups[group_name] = group
    result = dict(group)
    arn = group.get('GroupARN', '')
    if arn in store.tags:
        result['Tags'] = [{'Key': k, 'Value': v} for k, v in store.tags[arn].items()]
    return {'Group': result}