def handler(store, request: dict) -> dict:
    return store.tag_resource(
        ResourceArn=request["ResourceArn"],
        Tags=request["Tags"],
    )
