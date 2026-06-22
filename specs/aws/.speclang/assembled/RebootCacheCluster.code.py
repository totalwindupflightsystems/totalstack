
def reboot_cache_cluster(store, request):
    """Handle RebootCacheCluster — reboot cache nodes."""
    resource_name = request.get("CacheClusterId")
    if not resource_name:
        raise InvalidParameterValueException("CacheClusterId is required")
    if resource_name not in store.cache_clusters:
        raise CacheClusterNotFoundFault(f"Cache cluster {resource_name} not found")
    node_ids = request.get("CacheNodeIdsToReboot", [])
    if not node_ids:
        raise InvalidParameterValueException("CacheNodeIdsToReboot is required")
    # Simulate reboot
    return {"CacheClusterId": resource_name, "Status": "rebooting cache cluster nodes"}
