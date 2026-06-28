def handler(store, request: dict) -> dict:
    snap_ids = request.get("SnapshotIds", [])
    if snap_ids:
        records = []
        for sid in snap_ids:
            try:
                records.append(store.get_snapshot(sid).to_dict())
            except SnapshotNotFound:
                pass
        return {"Snapshots": records}
    return {"Snapshots": [r.to_dict() for r in store.snapshots()]}
