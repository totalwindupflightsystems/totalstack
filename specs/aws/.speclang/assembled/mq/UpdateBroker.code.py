def handler(store, request: dict) -> dict:
    return store.update_broker(**request)
