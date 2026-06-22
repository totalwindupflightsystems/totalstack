def handler(store, request: dict) -> dict:
    record = store.describe_cluster(request["ClusterId"])
    return {"Cluster": record.to_dict()}
