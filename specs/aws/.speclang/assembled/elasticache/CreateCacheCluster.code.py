# spec:trace: aws/elasticache/CreateCacheCluster.spec.py.md#implementation
# spec:id: @specs/aws/elasticache/createcachecluster
# spec:generated: DO NOT EDIT — edit the spec instead

def create_cache_cluster(store, request):
    """Handle CreateCacheCluster — create a new resource."""
    if "CacheClusterId" not in request or not request["CacheClusterId"]:
        raise InvalidParameterValueException("CacheClusterId is required")
    resource_name = request["CacheClusterId"]
    if resource_name in store.cache_clusters:
        raise CacheClusterAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"
    record.setdefault("Engine", "redis")
    record.setdefault("CacheNodeType", "cache.t2.micro")
    record.setdefault("NumCacheNodes", 1)

    store.cache_clusters[resource_name] = record

    # Build response
    response = {}
    response["CacheClusterId"] = resource_name
    response["Status"] = "available"
    response["CacheNodeType"] = record.get("CacheNodeType", "cache.t2.micro")
    response["Engine"] = record.get("Engine", "redis")
    response["NumCacheNodes"] = record.get("NumCacheNodes", 1)
    return response

