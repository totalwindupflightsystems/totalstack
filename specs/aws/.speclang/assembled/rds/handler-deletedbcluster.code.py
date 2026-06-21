def handler(store, request: dict) -> dict:
    identifier = request["DBClusterIdentifier"]
    skip = request.get("SkipFinalSnapshot", True)
    return store.delete_cluster(identifier, skip)
