# spec:trace: aws/elasticache/ModifyCacheParameterGroup.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/modifycacheparametergroup
# spec:generated: DO NOT EDIT — edit the spec instead

def modify_cache_parameter_group(store, request):
    """Handle ModifyCacheParameterGroup — modify a resource."""
    resource_name = request.get("CacheParameterGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheParameterGroupName is required")
    if resource_name not in store.parameter_groups:
        raise CacheParameterGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.parameter_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["CacheParameterGroupName"] = resource_name
    return response

