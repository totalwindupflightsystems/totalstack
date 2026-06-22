def handler(store, request: dict) -> dict:
    return store.update_nodegroup_version(
        clusterName=request["clusterName"],
        nodegroupName=request["nodegroupName"],
        version=request.get("version"))
