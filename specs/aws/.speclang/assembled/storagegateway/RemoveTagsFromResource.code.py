def remove_tags_from_resource(store, request: dict) -> dict:
    return store.remove_tags_from_resource(
        ResourceARN=request["ResourceARN"],
        TagKeys=request["TagKeys"],
    )
