def handler(store, request: dict) -> dict:
    if not request.get("BackupId"):
        raise BadRequest("BackupId is required")
    if not request.get("Name"):
        raise BadRequest("Name is required")
    _ = store.get_backup(request["BackupId"])
    kwargs = {k: v for k, v in request.items()
              if k != "BackupId"}
    record = store.create_volume(**kwargs)
    return record.to_dict()
