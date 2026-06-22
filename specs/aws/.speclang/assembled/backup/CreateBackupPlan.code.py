def handler(store, request: dict) -> dict:
    return store.create_backup_plan(**request)
