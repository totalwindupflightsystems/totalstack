def handler(store, request: dict) -> dict:
    return store.delete_addon(
        clusterName=request["clusterName"],
        addonName=request["addonName"])
