def handler(store, request: dict) -> dict:
    return store.describe_cluster(name=request["name"])
