def handler(store, request: dict) -> dict:
    return store.untag_resource(
        resourceShareArn=request.get("resourceShareArn"),
        tagKeys=request["tagKeys"],
        resourceArn=request.get("resourceArn"),
    )
