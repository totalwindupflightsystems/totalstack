# spec:trace: aws/elasticache/DeleteCacheSubnetGroup.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/deletecachesubnetgroup
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_cache_subnet_group(store, request):
    """Handle DeleteCacheSubnetGroup — delete a resource."""
    resource_name = request.get("CacheSubnetGroupName")
    if not resource_name:
        raise InvalidParameterValueException("CacheSubnetGroupName is required")
    if resource_name not in store.subnet_groups:
        raise CacheSubnetGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.subnet_groups[resource_name]
    return {}

