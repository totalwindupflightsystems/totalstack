def handler(store, request: dict) -> dict:
    store.tag_resource(request["ResourceArn"], request["Tags"])
    return {}
