def handler(store, request: dict) -> dict:
    return store.list_nodegroups(clusterName=request["clusterName"])
