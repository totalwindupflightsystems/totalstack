def handler(store, request: dict) -> dict:
    return store.untag_resource(resourceArn=request["resourceArn"], tagKeys=request["tagKeys"])
