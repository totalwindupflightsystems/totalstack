def handler(store, request: dict) -> dict:
    if not request.get("BackupId"):
        raise BadRequest("BackupId is required")
    _ = store.get_backup(request["BackupId"])
    if not request.get("SubnetIds"):
        raise BadRequest("SubnetIds is required")
    record = store.create_file_system(
        FileSystemType=request.get("FileSystemType", "WINDOWS"),
        **{k: v for k, v in request.items()
           if k not in ("BackupId", "FileSystemType")})
    return record.to_dict()
