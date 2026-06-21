// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/DescribeCacheParameterGroups.spec.py.md#input-shape-describecacheparametergroupsmessage
// spec:generated DO NOT EDIT — edit the spec instead

def describe_cache_parameter_groups(store, request):
    """Handle DescribeCacheParameterGroups — describe resources."""
    resource_name = request.get("CacheParameterGroupName")
    if resource_name:
        if resource_name not in store.parameter_groups:
            raise CacheParameterGroupNotFoundFault(f"Resource {resource_name} not found")
        return {CacheParameterGroups: [dict(store.parameter_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.parameter_groups.values()]
        return {CacheParameterGroups: items}