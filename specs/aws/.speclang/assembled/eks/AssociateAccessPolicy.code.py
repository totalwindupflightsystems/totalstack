def handler(store, request: dict) -> dict:
    return store.associate_access_policy(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"],
        policyArn=request["policyArn"],
        accessScope=request.get("accessScope"))
