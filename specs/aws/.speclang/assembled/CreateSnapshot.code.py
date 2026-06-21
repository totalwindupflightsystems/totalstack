// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/CreateSnapshot.spec.py.md#input-shape-createsnapshotmessage
// spec:generated DO NOT EDIT — edit the spec instead

def create_snapshot(store, request):
    """Handle CreateSnapshot — create a new resource."""
    if "SnapshotName" not in request or not request["SnapshotName"]:
        raise InvalidParameterValueException("SnapshotName is required")
    resource_name = request["SnapshotName"]
    if resource_name in store.snapshots:
        raise SnapshotAlreadyExistsFault(f"Resource {resource_name} already exists")

    # Build record from request
    record = {k: v for k, v in request.items()}
    record["Status"] = "available"

    store.snapshots[resource_name] = record

    # Build response
    response = {}
    response["SnapshotName"] = resource_name
    response["Status"] = "available"
    return response