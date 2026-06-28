def handler(store, request: dict) -> dict:
    return store.list_resources(
        resourceOwner=request.get("resourceOwner", "SELF"),
        principal=request.get("principal"),
        resourceType=request.get("resourceType"),
        resourceArns=request.get("resourceArns"),
        resourceShareArns=request.get("resourceShareArns"),
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
        resourceRegionScope=request.get("resourceRegionScope"),
    )
