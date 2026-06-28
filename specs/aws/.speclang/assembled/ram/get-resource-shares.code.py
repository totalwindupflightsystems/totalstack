def handler(store, request: dict) -> dict:
    return store.get_resource_shares(
        resourceShareArns=request.get("resourceShareArns"),
        resourceShareStatus=request.get("resourceShareStatus"),
        resourceOwner=request.get("resourceOwner", "SELF"),
        name=request.get("name"),
        tagFilters=request.get("tagFilters"),
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
        permissionArn=request.get("permissionArn"),
        permissionVersion=request.get("permissionVersion"),
    )
