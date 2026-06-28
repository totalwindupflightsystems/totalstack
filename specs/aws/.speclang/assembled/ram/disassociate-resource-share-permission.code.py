def handler(store, request: dict) -> dict:
    return store.disassociate_resource_share_permission(
        request["resourceShareArn"],
        request["permissionArn"],
        clientToken=request.get("clientToken"),
    )
