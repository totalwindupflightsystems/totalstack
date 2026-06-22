def handler(store, request: dict):
    return store.delete_cluster(request["DBClusterIdentifier"])
