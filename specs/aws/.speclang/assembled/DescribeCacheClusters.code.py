
def describe_cache_clusters(store, request):
    """Handle DescribeCacheClusters — describe resources."""
    resource_name = request.get("CacheClusterId")
    if resource_name:
        if resource_name not in store.cache_clusters:
            raise CacheClusterNotFoundFault(f"Resource {resource_name} not found")
        return {CacheClusters: [dict(store.cache_clusters[resource_name])]}
    else:
        items = [dict(v) for v in store.cache_clusters.values()]
        return {CacheClusters: items}
