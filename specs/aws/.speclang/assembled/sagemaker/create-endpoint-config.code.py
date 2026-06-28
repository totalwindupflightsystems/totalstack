def create_endpoint_config(store, request: dict) -> dict:
    return store.create_endpoint_config(**request)
