def list_tags_for_resource(store, request: dict) -> dict:
    return store.list_tags_for_resource(ResourceArn=request["ResourceArn"])
