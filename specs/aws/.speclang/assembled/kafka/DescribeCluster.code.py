def describe_cluster(store, request: dict) -> dict:
    return store.get_cluster(request["ClusterArn"])
