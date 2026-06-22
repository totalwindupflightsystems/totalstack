
def delete_user_group(store, request):
    """Handle DeleteUserGroup — delete a resource."""
    resource_name = request.get("UserGroupId")
    if not resource_name:
        raise InvalidParameterValueException("UserGroupId is required")
    if resource_name not in store.user_groups:
        raise UserGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.user_groups[resource_name]
    return {}
