def handler(store, request: dict) -> dict:
    store.delete_backup(request["BackupId"])
    return {}
