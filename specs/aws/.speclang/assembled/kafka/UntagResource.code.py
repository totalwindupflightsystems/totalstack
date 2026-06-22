def untag_resource(store, request: dict) -> dict:
    return store.untag_resource(request["ResourceArn"], request["TagKeys"])
