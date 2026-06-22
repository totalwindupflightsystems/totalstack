def handler(store, request: dict) -> dict:
    kwargs = {}
    if "resourcesVpcConfig" in request:
        kwargs["resourcesVpcConfig"] = request["resourcesVpcConfig"]
    if "logging" in request:
        kwargs["logging"] = request["logging"]
    if "accessConfig" in request:
        kwargs["accessConfig"] = request["accessConfig"]
    if "upgradePolicy" in request:
        kwargs["upgradePolicy"] = request["upgradePolicy"]
    return store.update_cluster_config(name=request["name"], **kwargs)
