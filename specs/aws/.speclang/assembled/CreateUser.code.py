// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/CreateUser.spec.py.md#input-shape-createusermessage
// spec:generated DO NOT EDIT — edit the spec instead

def create_user(store, request):
    """Handle CreateUser — create a new resource."""
    if "UserId" not in request or not request["UserId"]:
        raise InvalidParameterValueException("UserId is required")
    if "UserName" not in request or not request["UserName"]:
        raise InvalidParameterValueException("UserName is required")
    if "Engine" not in request or not request["Engine"]:
        raise InvalidParameterValueException("Engine is required")
    if "AccessString" not in request or not request["AccessString"]:
        raise InvalidParameterValueException("AccessString is required")
    resource_name = request["UserId"]
    if resource_name in store.users:
        raise UserAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.users[resource_name] = record

    # Build response
    response = {}
    response["UserId"] = resource_name
    response["Status"] = "available"
    return response