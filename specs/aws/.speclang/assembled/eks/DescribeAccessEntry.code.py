def handler(store, request: dict) -> dict:
    return store.describe_access_entry(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"])
