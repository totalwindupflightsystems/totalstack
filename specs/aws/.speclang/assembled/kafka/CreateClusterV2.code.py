def create_cluster_v2(store, request: dict) -> dict:
    return store.create_cluster(**request)
