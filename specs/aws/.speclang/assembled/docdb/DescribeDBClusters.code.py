def handler(store, request: dict):
    return store.describe_clusters(request.get("DBClusterIdentifier"), **{k: v for k, v in request.items() if k != "DBClusterIdentifier"})
