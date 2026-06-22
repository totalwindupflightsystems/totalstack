def handler(store, request: dict) -> dict:
    return store.delete_backup_selection(BackupPlanId=request["BackupPlanId"],SelectionId=request["SelectionId"])
