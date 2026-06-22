def handler(store, request: dict) -> dict:
    return store.describe_addon(
        clusterName=request["clusterName"],
        addonName=request["addonName"])
