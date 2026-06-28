def handler(store, request: dict) -> dict:
    if not request.get("SourceBackupId"):
        raise BadRequest("SourceBackupId is required")
    kwargs = {k: v for k, v in request.items()
              if k != "SourceBackupId"}
    record = store.copy_backup(request["SourceBackupId"], **kwargs)
    return record.to_dict()
