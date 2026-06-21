// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/CreateReplicationGroup.spec.py.md#input-shape-createreplicationgroupmessage
// spec:generated DO NOT EDIT — edit the spec instead

def create_replication_group(store, request):
    """Handle CreateReplicationGroup — create a new resource."""
    if "ReplicationGroupId" not in request or not request["ReplicationGroupId"]:
        raise InvalidParameterValueException("ReplicationGroupId is required")
    if "ReplicationGroupDescription" not in request or not request["ReplicationGroupDescription"]:
        raise InvalidParameterValueException("ReplicationGroupDescription is required")
    resource_name = request["ReplicationGroupId"]
    if resource_name in store.replication_groups:
        raise ReplicationGroupAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"
    record.setdefault("Status", "available")

    store.replication_groups[resource_name] = record

    # Build response
    response = {}
    response["ReplicationGroupId"] = resource_name
    response["Status"] = "available"
    return response