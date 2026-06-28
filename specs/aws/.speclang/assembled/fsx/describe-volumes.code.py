def handler(store, request: dict) -> dict:
    vol_ids = request.get("VolumeIds", [])
    if vol_ids:
        records = []
        for vid in vol_ids:
            try:
                records.append(store.get_volume(vid).to_dict())
            except VolumeNotFound:
                pass
        return {"Volumes": records}
    return {"Volumes": [r.to_dict() for r in store.volumes()]}
