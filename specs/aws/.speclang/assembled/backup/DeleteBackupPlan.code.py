def handler(store, request: dict) -> dict:
    return store.delete_backup_plan(BackupPlanId=request["BackupPlanId"])
