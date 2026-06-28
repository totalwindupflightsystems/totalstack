def handler(store, request: dict) -> dict:
    return store.associate_resource_share_permission(
        request["resourceShareArn"],
        request["permissionArn"],
        replace=request.get("replace", False),
        clientToken=request.get("clientToken"),
        permissionVersion=request.get("permissionVersion"),
    )
