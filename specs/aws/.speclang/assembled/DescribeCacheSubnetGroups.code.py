// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/DescribeCacheSubnetGroups.spec.py.md#input-shape-describecachesubnetgroupsmessage
// spec:generated DO NOT EDIT — edit the spec instead

def describe_cache_subnet_groups(store, request):
    """Handle DescribeCacheSubnetGroups — describe resources."""
    resource_name = request.get("CacheSubnetGroupName")
    if resource_name:
        if resource_name not in store.subnet_groups:
            raise CacheSubnetGroupNotFoundFault(f"Resource {resource_name} not found")
        return {CacheSubnetGroups: [dict(store.subnet_groups[resource_name])]}
    else:
        items = [dict(v) for v in store.subnet_groups.values()]
        return {CacheSubnetGroups: items}