def handler(store, request: dict) -> dict:
    kwargs = {}
    if "kubernetesGroups" in request:
        kwargs["kubernetesGroups"] = request["kubernetesGroups"]
    if "username" in request:
        kwargs["username"] = request["username"]
    return store.update_access_entry(
        clusterName=request["clusterName"],
        principalArn=request["principalArn"], **kwargs)
