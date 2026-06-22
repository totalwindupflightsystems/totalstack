def handler(store, request: dict) -> dict:
    return store.create_tags(ResourceArn=request["ResourceArn"], Tags=request.get("Tags", {}))
