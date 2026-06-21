def handler(store, request: dict) -> dict:
    identifier = request["DBClusterIdentifier"]
    kwargs = {k: v for k, v in request.items() if k != "DBClusterIdentifier" and v is not None}
    return store.modify_cluster(identifier, **kwargs)
