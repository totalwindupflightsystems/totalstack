def handler(store, request: dict) -> dict:
    return store.create_broker(**request)
