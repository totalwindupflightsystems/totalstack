def handler(store, request: dict) -> dict:
    return store.list_permission_versions(
        request["permissionArn"],
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
