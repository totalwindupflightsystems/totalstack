# spec:trace: aws/elasticache/DeleteCacheCluster.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/deletecachecluster
# spec:generated: DO NOT EDIT — edit the spec instead

def delete_cache_cluster(store, request):
    """Handle DeleteCacheCluster — delete a resource."""
    resource_name = request.get("CacheClusterId")
    if not resource_name:
        raise InvalidParameterValueException("CacheClusterId is required")
    if resource_name not in store.cache_clusters:
        raise CacheClusterNotFoundFault(f"Resource {resource_name} not found")
    del store.cache_clusters[resource_name]
    return {}

