def handler(store, request: dict) -> dict:
    return store.get_resource_share_associations(
        request["associationType"],
        resourceShareArns=request.get("resourceShareArns"),
        resourceArn=request.get("resourceArn"),
        principal=request.get("principal"),
        associationStatus=request.get("associationStatus"),
        nextToken=request.get("nextToken"),
        maxResults=request.get("maxResults"),
    )
