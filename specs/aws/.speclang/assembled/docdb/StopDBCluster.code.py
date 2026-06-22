def handler(store, request: dict):
    return store.stop_cluster(request["DBClusterIdentifier"])
