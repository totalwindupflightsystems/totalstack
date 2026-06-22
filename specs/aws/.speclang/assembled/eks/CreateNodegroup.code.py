def handler(store, request: dict) -> dict:
    return store.create_nodegroup(
        clusterName=request["clusterName"],
        nodegroupName=request["nodegroupName"],
        scalingConfig=request.get("scalingConfig"),
        subnets=request.get("subnets"),
        instanceTypes=request.get("instanceTypes"),
        amiType=request.get("amiType"),
        tags=request.get("tags"),
    )
