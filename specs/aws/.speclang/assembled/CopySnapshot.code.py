// spec:trace spec=/home/kara/totalstack/specs/aws/elasticache/CopySnapshot.spec.py.md#input-shape-copysnapshotmessage
// spec:generated DO NOT EDIT — edit the spec instead

def copy_snapshot(store, request):
    """Handle CopySnapshot — copy a snapshot."""
    source = request.get("SourceSnapshotName")
    target = request.get("TargetSnapshotName")
    if not source or not target:
        raise InvalidParameterValueException("SourceSnapshotName and TargetSnapshotName are required")
    if source not in store.snapshots:
        raise SnapshotNotFoundFault(f"Snapshot {source} not found")
    if target in store.snapshots:
        raise SnapshotAlreadyExistsFault(f"Snapshot {target} already exists")
    # Copy snapshot record
    store.snapshots[target] = dict(store.snapshots[source])
    store.snapshots[target]["SnapshotName"] = target
    return {"Snapshot": store.snapshots[target]}