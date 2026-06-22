def handler(store, request: dict) -> dict:
    return store.delete_nodegroup(
        clusterName=request["clusterName"],
        nodegroupName=request["nodegroupName"])
