def handler(store, request: dict) -> dict:
    return store.delete_permission_version(
        request["permissionArn"],
        request["permissionVersion"],
        clientToken=request.get("clientToken"),
    )
