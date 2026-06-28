def handler(store, request: dict) -> dict:
    return store.delete_permission(
        request["permissionArn"],
        clientToken=request.get("clientToken"),
    )
