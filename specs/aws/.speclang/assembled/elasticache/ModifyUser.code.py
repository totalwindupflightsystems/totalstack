# spec:trace: aws/elasticache/ModifyUser.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/modifyuser
# spec:generated: DO NOT EDIT — edit the spec instead

def modify_user(store, request):
    """Handle ModifyUser — modify a resource."""
    resource_name = request.get("UserId")
    if not resource_name:
        raise InvalidParameterValueException("UserId is required")
    if resource_name not in store.users:
        raise UserNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.users[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["UserId"] = resource_name
    return response

