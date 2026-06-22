def handler(store, request: dict) -> dict:
    return store.disassociate_access_policy(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"],
        policyArn=request["policyArn"])
