def handler(store, request: dict) -> dict:
    return store.list_tags_for_resource(
        resource_arn=request["resourceArn"],
    )
