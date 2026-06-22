def handler(store, request: dict):
    return store.modify_cluster(request["DBClusterIdentifier"], **{k: v for k, v in request.items() if k != "DBClusterIdentifier"})
