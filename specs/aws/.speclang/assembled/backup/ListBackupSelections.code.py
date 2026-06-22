def handler(store, request: dict) -> dict:
    return store.list_backup_selections(BackupPlanId=request["BackupPlanId"],MaxResults=request.get("MaxResults"))
