def handler(store, request: dict) -> dict:
    return store.untag_resource(ResourceArn=request["ResourceArn"],TagKeys=request.get("TagKeys",[]))
