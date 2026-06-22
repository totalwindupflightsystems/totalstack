def handler(store, request: dict) -> dict:
    return store.list_tags_for_resource(resourceArn=request["resourceArn"])
