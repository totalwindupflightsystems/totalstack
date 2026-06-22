def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k != "ClusterIdentifier"}
    record = store.resize_cluster(request["ClusterIdentifier"], **kwargs)
    return {"Cluster": record.to_dict()}
