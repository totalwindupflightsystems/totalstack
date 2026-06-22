def handler(store, request: dict) -> dict:
    return store.describe_fargate_profile(
        clusterName=request["clusterName"],
        fargateProfileName=request["fargateProfileName"])
