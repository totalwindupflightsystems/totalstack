def handler(store, request: dict) -> dict:
    return store.create_addon(
        clusterName=request["clusterName"],
        addonName=request["addonName"],
        addonVersion=request.get("addonVersion"),
        serviceAccountRoleArn=request.get("serviceAccountRoleArn"),
        tags=request.get("tags"),
    )
