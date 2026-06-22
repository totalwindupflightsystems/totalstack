def handler(store, request: dict) -> dict:
    return store.list_associated_access_policies(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"])
