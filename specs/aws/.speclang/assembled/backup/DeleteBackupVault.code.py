def handler(store, request: dict) -> dict:
    return store.delete_backup_vault(BackupVaultName=request["BackupVaultName"])
