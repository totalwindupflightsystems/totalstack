def handler(store, request: dict) -> dict:
    return store.delete_fargate_profile(
        clusterName=request["clusterName"],
        fargateProfileName=request["fargateProfileName"])
