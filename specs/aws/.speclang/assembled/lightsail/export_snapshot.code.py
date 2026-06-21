# spec:trace: aws/lightsail/export_snapshot.spec.py.md#implementation
# spec:id: @specs/aws/lightsail/export-snapshot
# spec:generated: DO NOT EDIT — edit the spec instead

def export_snapshot(store, request: dict) -> dict:
    """Exports an Amazon Lightsail instance or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2). This operation results in an export snapshot record that can be used with the create c"""
    source_snapshot_name = request.get("sourceSnapshotName", "").strip() if isinstance(request.get("sourceSnapshotName"), str) else request.get("sourceSnapshotName")
    if not source_snapshot_name:
        raise ValidationException("sourceSnapshotName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("ExportSnapshot", request)

