
def create_group(store: 'XrayStore', request: dict) -> dict:
    """Create a new X-Ray group."""
    group_name = request.get('GroupName')
    if not group_name:
        raise InvalidRequestException('GroupName is required')

    groups = store.groups
    if group_name in groups:
        raise InvalidRequestException(f'Group {group_name} already exists')

    group_arn = f'arn:aws:xray:us-east-1:000000000000:group/{group_name}'
    group = {
        'GroupName': group_name,
        'GroupARN': group_arn,
        'FilterExpression': request.get('FilterExpression', ''),
        'InsightsConfiguration': request.get('InsightsConfiguration', {
            'InsightsEnabled': False,
            'NotificationsEnabled': False
        }),
    }

    # Handle tags
    tags = request.get('Tags', [])
    if tags:
        store.tags[group_arn] = {t['Key']: t['Value'] for t in tags}

    groups[group_name] = group
    result = dict(group)
    if tags:
        result['Tags'] = tags
    return {'Group': result}
