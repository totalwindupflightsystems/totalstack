# spec:trace: aws/elasticache/ModifyCacheCluster.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/modifycachecluster
# spec:generated: DO NOT EDIT — edit the spec instead

def modify_cache_cluster(store, request):
    """Handle ModifyCacheCluster — modify a resource."""
    resource_name = request.get("CacheClusterId")
    if not resource_name:
        raise InvalidParameterValueException("CacheClusterId is required")
    if resource_name not in store.cache_clusters:
        raise CacheClusterNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.cache_clusters[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["CacheClusterId"] = resource_name
    return response

