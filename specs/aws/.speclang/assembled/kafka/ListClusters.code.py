def list_clusters(store, request: dict) -> dict:
    return {"ClusterInfoList": store.list_clusters(**request)}
