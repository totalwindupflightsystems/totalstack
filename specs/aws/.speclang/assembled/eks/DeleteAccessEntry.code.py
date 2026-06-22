def handler(store, request: dict) -> dict:
    return store.delete_access_entry(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"])
