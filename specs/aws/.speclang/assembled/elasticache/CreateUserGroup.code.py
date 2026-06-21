# spec:trace: aws/elasticache/CreateUserGroup.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/createusergroup
# spec:generated: DO NOT EDIT — edit the spec instead

def create_user_group(store, request):
    """Handle CreateUserGroup — create a new resource."""
    if "UserGroupId" not in request or not request["UserGroupId"]:
        raise InvalidParameterValueException("UserGroupId is required")
    if "Engine" not in request or not request["Engine"]:
        raise InvalidParameterValueException("Engine is required")
    resource_name = request["UserGroupId"]
    if resource_name in store.user_groups:
        raise UserGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.user_groups[resource_name] = record

    # Build response
    response = {}
    response["UserGroupId"] = resource_name
    response["Status"] = "available"
    return response

