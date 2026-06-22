def handler(store, request: dict):
    return store.start_cluster(request["DBClusterIdentifier"])
