
def delete_snapshot(store, request):
    """Handle DeleteSnapshot — delete a resource."""
    resource_name = request.get("SnapshotName")
    if not resource_name:
        raise InvalidParameterValueException("SnapshotName is required")
    if resource_name not in store.snapshots:
        raise SnapshotNotFoundFault(f"Resource {resource_name} not found")
    del store.snapshots[resource_name]
    return {}
