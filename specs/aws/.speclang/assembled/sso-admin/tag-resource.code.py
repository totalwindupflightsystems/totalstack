def handler(store, request: dict) -> dict:
    return store.tag_resource(request["resourceArn"], request["tags"])
