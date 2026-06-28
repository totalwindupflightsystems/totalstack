def handler(store, request: dict) -> dict:
    return store.create_resource_share(
        name=request["name"],
        resourceArns=request.get("resourceArns"),
        principals=request.get("principals"),
        tags=request.get("tags"),
        allowExternalPrincipals=request.get("allowExternalPrincipals"),
        clientToken=request.get("clientToken"),
        permissionArns=request.get("permissionArns"),
        sources=request.get("sources"),
    )
