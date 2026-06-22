def handler(store, request: dict) -> dict:
    return store.untag_resource(
        resource_arn=request["resourceArn"],
        tag_keys=request["tagKeys"],
    )
