
def modify_cache_subnet_group(store, request):
    """Handle ModifyCacheSubnetGroup — modify a resource."""
    resource_name = request.get("CacheSubnetGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheSubnetGroupName is required")
    if resource_name not in store.subnet_groups:
        raise CacheSubnetGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.subnet_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["CacheSubnetGroupName"] = resource_name
    return response
