def handler(store, request: dict) -> dict:
    return store.list_access_entries(clusterName=request["clusterName"])
