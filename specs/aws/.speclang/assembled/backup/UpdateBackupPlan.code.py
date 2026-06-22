def handler(store, request: dict) -> dict:
    return store.update_backup_plan(**request)
