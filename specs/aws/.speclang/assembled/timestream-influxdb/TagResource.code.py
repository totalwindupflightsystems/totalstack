def handler(store, request: dict) -> dict:
    return store.tag_resource(
        resourceArn=request["resourceArn"],
        tags=request["tags"],
    )
