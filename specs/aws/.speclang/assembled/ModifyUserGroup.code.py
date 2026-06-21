// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/ModifyUserGroup.spec.py.md#input-shape-modifyusergroupmessage
// spec:generated DO NOT EDIT — edit the spec instead

def modify_user_group(store, request):
    """Handle ModifyUserGroup — modify a resource."""
    resource_name = request.get("UserGroupId")
    if not resource_name:
        raise InvalidParameterValueException("UserGroupId is required")
    if resource_name not in store.user_groups:
        raise UserGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.user_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["UserGroupId"] = resource_name
    return response