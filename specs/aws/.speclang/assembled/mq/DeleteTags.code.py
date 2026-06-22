def handler(store, request: dict) -> dict:
    return store.delete_tags(ResourceArn=request["ResourceArn"], TagKeys=request.get("TagKeys", []))
