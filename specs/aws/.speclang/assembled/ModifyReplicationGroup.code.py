
def modify_replication_group(store, request):
    """Handle ModifyReplicationGroup — modify a resource."""
    resource_name = request.get("ReplicationGroupId")
    if not resource_name:
        raise InvalidParameterValueException("ReplicationGroupId is required")
    if resource_name not in store.replication_groups:
        raise ReplicationGroupNotFoundFault(f"Resource {resource_name} not found")

    # Update fields from request
    record = store.replication_groups[resource_name]
    for key, value in request.items():
        if value is not None:
            record[key] = value

    # Build response with updated fields
    response = dict(record)
    response["ReplicationGroupId"] = resource_name
    return response
