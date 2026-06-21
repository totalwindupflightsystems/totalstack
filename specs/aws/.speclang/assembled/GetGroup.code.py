// spec:trace spec=/home/kara/totalstack/specs/aws/xray/GetGroup.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def get_group(store, request):
    group_name = request.get('GroupName', '')
    group_arn = request.get('GroupARN', '')

    if not group_name and not group_arn:
        raise InvalidRequestException('GroupName or GroupARN is required')

    groups = store.groups
    if group_arn:
        group = next((g for g in groups.values() if g.get('GroupARN') == group_arn), None)
    else:
        group = groups.get(group_name)

    if not group:
        raise InvalidRequestException(f'Group not found')

    result = dict(group)
    arn = group.get('GroupARN', '')
    if arn in store.tags:
        result['Tags'] = [{'Key': k, 'Value': v} for k, v in store.tags[arn].items()]
    return {'Group': result}