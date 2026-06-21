def handler(store, request: dict) -> dict:
    identifier = request.get("DBClusterIdentifier")
    return store.describe_clusters(identifier)
