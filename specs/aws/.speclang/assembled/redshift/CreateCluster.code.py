def handler(store, request: dict) -> dict:
    kwargs = {k: v for k, v in request.items() if k != "ClusterIdentifier" and k != "NodeType" and k != "MasterUsername"}
    record = store.create_cluster(request["ClusterIdentifier"], request["NodeType"], request["MasterUsername"], **kwargs)
    return {"Cluster": record.to_dict()}
