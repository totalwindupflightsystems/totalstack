def handler(store, request: dict) -> dict:
    return store.tag_resource(
        resourceShareArn=request.get("resourceShareArn"),
        tags=request["tags"],
        resourceArn=request.get("resourceArn"),
    )
