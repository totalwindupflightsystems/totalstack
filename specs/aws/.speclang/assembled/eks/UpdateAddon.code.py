def handler(store, request: dict) -> dict:
    kwargs = {}
    if "addonVersion" in request:
        kwargs["addonVersion"] = request["addonVersion"]
    if "serviceAccountRoleArn" in request:
        kwargs["serviceAccountRoleArn"] = request["serviceAccountRoleArn"]
    return store.update_addon(
        clusterName=request["clusterName"],
        addonName=request["addonName"], **kwargs)
