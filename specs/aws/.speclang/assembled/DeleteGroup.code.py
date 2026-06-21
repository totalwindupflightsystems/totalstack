// spec:trace spec=/home/kara/totalstack/specs/aws/xray/DeleteGroup.spec.py.md#implementation
// spec:generated DO NOT EDIT — edit the spec instead

def delete_group(store, request):
    group_name = request.get('GroupName', '')
    group_arn = request.get('GroupARN', '')
    if not group_name and not group_arn:
        raise InvalidRequestException('GroupName or GroupARN is required')
    groups = store.groups
    if group_arn:
        group = next((g for g in groups.values() if g.get('GroupARN') == group_arn), None)
        if group:
            group_name = group['GroupName']
    if group_name not in groups:
        raise InvalidRequestException(f'Group not found')
    group = groups.pop(group_name)
    arn = group.get('GroupARN', '')
    store.tags.pop(arn, None)
    return {}