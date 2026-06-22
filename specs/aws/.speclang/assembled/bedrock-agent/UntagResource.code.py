def handler(store, request: dict) -> dict:
    return store.untag_resource(request["resourceArn"], request["tagKeys"])
