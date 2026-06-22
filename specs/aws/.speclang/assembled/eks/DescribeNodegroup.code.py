def handler(store, request: dict) -> dict:
    return store.describe_nodegroup(
        clusterName=request["clusterName"],
        nodegroupName=request["nodegroupName"])
