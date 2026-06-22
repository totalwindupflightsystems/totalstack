def handler(store, request: dict) -> dict:
    return store.create_fargate_profile(
        clusterName=request["clusterName"],
        fargateProfileName=request["fargateProfileName"],
        podExecutionRoleArn=request["podExecutionRoleArn"],
        subnets=request.get("subnets"),
        selectors=request.get("selectors"),
        tags=request.get("tags"),
    )
