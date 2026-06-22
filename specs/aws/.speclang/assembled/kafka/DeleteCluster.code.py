def delete_cluster(store, request: dict) -> dict:
    return store.delete_cluster(request["ClusterArn"])
