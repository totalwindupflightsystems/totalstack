def handler(store, request: dict) -> dict:
    return store.list_resource_share_permissions(
        request["resourceShareArn"],
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
