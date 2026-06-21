def handler(store, request: dict) -> dict:
    identifier = request["DBClusterIdentifier"]
    return store.create_cluster(identifier, Engine=request.get("Engine", "aurora-mysql"))
