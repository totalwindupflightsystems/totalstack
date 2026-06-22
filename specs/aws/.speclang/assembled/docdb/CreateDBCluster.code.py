def handler(store, request: dict):
    cluster_id = request["DBClusterIdentifier"]
    engine = request["Engine"]
    return store.create_cluster(cluster_id, engine, **{k: v for k, v in request.items() if k not in ("DBClusterIdentifier", "Engine")})
