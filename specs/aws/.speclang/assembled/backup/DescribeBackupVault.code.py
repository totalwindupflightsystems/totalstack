def handler(store, request: dict) -> dict:
    return store.describe_backup_vault(BackupVaultName=request["BackupVaultName"])
