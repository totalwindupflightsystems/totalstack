def handler(store, request: dict) -> dict:
    return store.stop_backup_job(BackupJobId=request["BackupJobId"])
