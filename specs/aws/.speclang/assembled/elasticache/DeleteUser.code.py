# spec:trace: aws/elasticache/DeleteUser.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/deleteuser
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_user(store, request):
    """Handle DeleteUser — delete a resource."""
    resource_name = request.get("UserId")
    if not resource_name:
        raise InvalidParameterValueException("UserId is required")
    if resource_name not in store.users:
        raise UserNotFoundFault(f"Resource {resource_name} not found")
    del store.users[resource_name]
    return {}

