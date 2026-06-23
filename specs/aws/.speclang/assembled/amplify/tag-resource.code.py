def handler(store, request: dict) -> dict:
    store.tag_resource(request["resourceArn"], request["tags"])
    return {}
