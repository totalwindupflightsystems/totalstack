def create_replication_task(store, request: dict) -> dict:
    return store.create_replication_task(**request)
