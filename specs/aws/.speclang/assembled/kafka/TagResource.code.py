def tag_resource(store, request: dict) -> dict:
    return store.tag_resource(request["ResourceArn"], request["Tags"])
