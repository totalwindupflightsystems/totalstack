def handler(store, request: dict) -> dict:
    """RemoveTagsFromResource handler."""
    return store.remove_tags_from_resource(
        resource_name=request["ResourceName"],
        tag_keys=request["TagKeys"])
