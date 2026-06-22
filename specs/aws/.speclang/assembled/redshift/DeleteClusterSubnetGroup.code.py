def handler(store, request: dict) -> dict:
    store.delete_cluster_subnet_group(request["ClusterSubnetGroupName"])
    return {}
