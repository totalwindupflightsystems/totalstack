def handler(store, request: dict) -> dict:
    return store.tag_resource(
        resource_arn=request["resourceArn"],
        tags=request["tags"],
    )
