
def delete_replication_group(store, request):
    """Handle DeleteReplicationGroup — delete a resource."""
    resource_name = request.get("ReplicationGroupId")
    if not resource_name:
        raise InvalidParameterValueException("ReplicationGroupId is required")
    if resource_name not in store.replication_groups:
        raise ReplicationGroupNotFoundFault(f"Resource {resource_name} not found")
    del store.replication_groups[resource_name]
    return {}
