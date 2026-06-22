def handler(store, request: dict) -> dict:
    return store.get_backup_plan(BackupPlanId=request["BackupPlanId"])
