def handler(store, request: dict) -> dict:
    record = store.pause_cluster(request["ClusterIdentifier"])
    return {"Cluster": record.to_dict()}
