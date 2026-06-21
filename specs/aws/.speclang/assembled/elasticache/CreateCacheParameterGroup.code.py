# spec:trace: aws/elasticache/CreateCacheParameterGroup.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/createcacheparametergroup
# spec:generated: DO NOT EDIT — edit the spec instead

def create_cache_parameter_group(store, request):
    """Handle CreateCacheParameterGroup — create a new resource."""
    if "CacheParameterGroupName" not in request or not request["CacheParameterGroupName"]:
        raise InvalidParameterValueException("CacheParameterGroupName is required")
    if "CacheParameterGroupFamily" not in request or not request["CacheParameterGroupFamily"]:
        raise InvalidParameterValueException("CacheParameterGroupFamily is required")
    if "Description" not in request or not request["Description"]:
        raise InvalidParameterValueException("Description is required")
    resource_name = request["CacheParameterGroupName"]
    if resource_name in store.parameter_groups:
        raise CacheParameterGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.parameter_groups[resource_name] = record

    # Build response
    response = {}
    response["CacheParameterGroupName"] = resource_name
    response["Status"] = "available"
    return response

