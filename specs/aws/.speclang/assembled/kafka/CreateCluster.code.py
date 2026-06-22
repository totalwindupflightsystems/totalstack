def create_cluster(store, request: dict) -> dict:
    return store.create_cluster(**request)
