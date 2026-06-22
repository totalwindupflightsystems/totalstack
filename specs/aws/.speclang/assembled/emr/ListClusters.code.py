def handler(store, request: dict) -> dict:
    clusters = store.list_clusters(ClusterStates=request.get("ClusterStates"))
    return {"Clusters": [c.to_dict() for c in clusters], "Marker": None}
