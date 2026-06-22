def handler(store, request: dict) -> dict:
    return store.create_cluster(
        name=request["name"],
        version=request.get("version"),
        roleArn=request["roleArn"],
        resourcesVpcConfig=request.get("resourcesVpcConfig"),
        kubernetesNetworkConfig=request.get("kubernetesNetworkConfig"),
        logging=request.get("logging"),
        tags=request.get("tags"),
    )
