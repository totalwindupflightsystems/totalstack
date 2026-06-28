def handler(store, request: dict) -> dict:
    return store.set_default_permission_version(
        request["permissionArn"],
        request["permissionVersion"],
        clientToken=request.get("clientToken"),
    )
