def handler(store, request: dict) -> dict:
    return store.delete_cluster(name=request["name"])
