// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/DescribeUserGroups.spec.py.md#input-shape-describeusergroupsmessage
// spec:generated DO NOT EDIT — edit the spec instead

def describe_user_groups(store, request):
    """Handle DescribeUserGroups — describe resources."""
    resource_name = request.get("UserGroupId")
    if resource_name:
        if resource_name not in store.user_groups:
            raise UserGroupNotFoundFault(f"Resource {resource_name} not found")
        return {UserGroups: [dict(store.user_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.user_groups.values()]
        return {UserGroups: items}