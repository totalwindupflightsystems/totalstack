def handler(store, request: dict) -> dict:
    record = store.reboot_cluster(request["ClusterIdentifier"])
    return {"Cluster": record.to_dict()}
