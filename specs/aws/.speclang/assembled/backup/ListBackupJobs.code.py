def handler(store, request: dict) -> dict:
    return store.list_backup_jobs(**request)
