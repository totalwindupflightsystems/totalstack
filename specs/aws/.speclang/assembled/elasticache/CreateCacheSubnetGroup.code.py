# spec:trace: aws/elasticache/CreateCacheSubnetGroup.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/createcachesubnetgroup
# spec:generated: DO NOT EDIT — edit the spec instead

def create_cache_subnet_group(store, request):
    """Handle CreateCacheSubnetGroup — create a new resource."""
    if "CacheSubnetGroupName" not in request or not request["CacheSubnetGroupName"]:
        raise InvalidParameterValueException("CacheSubnetGroupName is required")
    if "CacheSubnetGroupDescription" not in request or not request["CacheSubnetGroupDescription"]:
        raise InvalidParameterValueException("CacheSubnetGroupDescription is required")
    if "SubnetIds" not in request or not request["SubnetIds"]:
        raise InvalidParameterValueException("SubnetIds is required")
    resource_name = request["CacheSubnetGroupName"]
    if resource_name in store.subnet_groups:
        raise CacheSubnetGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.subnet_groups[resource_name] = record

    # Build response
    response = {}
    response["CacheSubnetGroupName"] = resource_name
    response["Status"] = "available"
    return response

