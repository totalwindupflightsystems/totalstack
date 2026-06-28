def handler(store, request: dict) -> dict:
    return store.create_permission_version(
        request["permissionArn"],
        request["policyTemplate"],
        clientToken=request.get("clientToken"),
    )
