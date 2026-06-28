def handler(store, request: dict) -> dict:
    fs_ids = request.get("FileSystemIds", [])
    if fs_ids:
        records = []
        for fid in fs_ids:
            try:
                records.append(store.get_file_system(fid).to_dict())
            except FileSystemNotFound:
                pass
        return {"FileSystems": records}
    return {"FileSystems": [r.to_dict() for r in store.file_systems()]}
