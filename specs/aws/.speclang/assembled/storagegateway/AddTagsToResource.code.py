def add_tags_to_resource(store, request: dict) -> dict:
    return store.add_tags_to_resource(
        ResourceARN=request["ResourceARN"],
        Tags=request["Tags"],
    )
