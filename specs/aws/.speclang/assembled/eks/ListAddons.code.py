def handler(store, request: dict) -> dict:
    return store.list_addons(clusterName=request["clusterName"])
