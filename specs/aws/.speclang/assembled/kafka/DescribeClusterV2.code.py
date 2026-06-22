def describe_cluster_v2(store, request: dict) -> dict:
    return store.get_cluster(request["ClusterArn"])
