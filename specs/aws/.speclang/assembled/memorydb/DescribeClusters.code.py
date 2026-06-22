def handler(store, request: dict) -> dict:
    cn = request.get("ClusterName")
    return store.describe_clusters(ClusterName=cn)

