def get_bootstrap_brokers(store, request: dict) -> dict:
    return store.get_bootstrap_brokers(request["ClusterArn"])
