def handler(store, request: dict) -> dict:
    kwargs = {}
    if "scalingConfig" in request:
        kwargs["scalingConfig"] = request["scalingConfig"]
    if "labels" in request:
        kwargs["labels"] = request.get("labels", {}).get("addOrUpdateLabels", {})
    if "taints" in request:
        kwargs["taints"] = request["taints"]
    return store.update_nodegroup_config(
        clusterName=request["clusterName"],
        nodegroupName=request["nodegroupName"], **kwargs)
