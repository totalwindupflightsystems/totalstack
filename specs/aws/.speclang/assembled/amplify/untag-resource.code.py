def handler(store, request: dict) -> dict:
    store.untag_resource(request["resourceArn"], request["tagKeys"])
    return {}
