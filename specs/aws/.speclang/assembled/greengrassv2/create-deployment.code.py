def create_deployment(store, request: dict) -> dict:
    return store.create_deployment(**request)
