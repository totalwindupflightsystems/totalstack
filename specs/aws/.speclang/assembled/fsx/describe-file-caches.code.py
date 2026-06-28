def handler(store, request: dict) -> dict:
    fc_ids = request.get("FileCacheIds", [])
    if fc_ids:
        records = []
        for fid in fc_ids:
            try:
                records.append(store.get_file_cache(fid).to_dict())
            except FileCacheNotFound:
                pass
        return {"FileCaches": records}
    return {"FileCaches": [r.to_dict() for r in store.file_caches()]}
