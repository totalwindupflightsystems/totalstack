# spec:trace: aws/lightsail/copy_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/copy-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def copy_snapshot(store, request: dict) -> dict:
    """Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manua"""
    source_region = request.get("sourceRegion", "").strip() if isinstance(request.get("sourceRegion"), str) else request.get("sourceRegion")
    if not source_region:
        raise ValidationException("sourceRegion is required")
    target_snapshot_name = request.get("targetSnapshotName", "").strip() if isinstance(request.get("targetSnapshotName"), str) else request.get("targetSnapshotName")
    if not target_snapshot_name:
        raise ValidationException("targetSnapshotName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CopySnapshot", request)

