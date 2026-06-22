def handler(store, request: dict) -> dict:
    return store.start_backup_job(**request)
