def handler(store, request: dict) -> dict:
    return store.describe_backup_job(BackupJobId=request["BackupJobId"])
