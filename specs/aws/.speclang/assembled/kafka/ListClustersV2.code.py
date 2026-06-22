def list_clusters_v2(store, request: dict) -> dict:
    return {"ClusterInfoList": store.list_clusters(**request)}
