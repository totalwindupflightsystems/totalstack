def handler(store, request: dict) -> dict:
    return store.update_resource_share(
        request["resourceShareArn"],
        name=request.get("name"),
        allowExternalPrincipals=request.get("allowExternalPrincipals"),
        clientToken=request.get("clientToken"),
    )
