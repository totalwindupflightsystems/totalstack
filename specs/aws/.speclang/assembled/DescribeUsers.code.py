
def describe_users(store, request):
    """Handle DescribeUsers — describe resources."""
    resource_name = request.get("UserId")
    if resource_name:
        if resource_name not in store.users:
            raise UserNotFoundFault(f"Resource {resource_name} not found")
        return {Users: [dict(store.users[resource_name])]}
    else:
        items = [dict(v) for v in store.users.values()]
        return {Users: items}
