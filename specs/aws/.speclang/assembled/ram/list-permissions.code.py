def handler(store, request: dict) -> dict:
    return store.list_permissions(
        resourceType=request.get("resourceType"),
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
        permissionType=request.get("permissionType"),
    )
