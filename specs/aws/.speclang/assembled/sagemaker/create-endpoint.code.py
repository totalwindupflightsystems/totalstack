def create_endpoint(store, request: dict) -> dict:
    return store.create_endpoint(**request)
