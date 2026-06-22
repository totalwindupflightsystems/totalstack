def handler(store, request: dict) -> dict:
    return store.create_access_entry(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"],
        kubernetesGroups=request.get("kubernetesGroups"),
        tags=request.get("tags"),
        username=request.get("username"),
    )
