def handler(store, request: dict) -> dict:
    return store.list_principals(
        resourceOwner=request.get("resourceOwner", "SELF"),
        resourceArn=request.get("resourceArn"),
        principals=request.get("principals"),
        resourceType=request.get("resourceType"),
        resourceShareArns=request.get("resourceShareArns"),
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
