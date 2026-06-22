def handler(store, request: dict) -> dict:
    return store.list_fargate_profiles(clusterName=request["clusterName"])
