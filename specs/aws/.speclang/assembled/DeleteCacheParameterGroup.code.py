
def delete_cache_parameter_group(store, request):
    """Handle DeleteCacheParameterGroup — delete a resource."""
    resource_name = request.get("CacheParameterGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheParameterGroupName is required")
    if resource_name not in store.parameter_groups:
        raise CacheParameterGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.parameter_groups[resource_name]
    return {}
