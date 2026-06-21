def handler(store, request: dict) -> dict:
    """AddTagsToResource handler."""
    return store.add_tags_to_resource(
        resource_name=request["ResourceName"],
        tags=request["Tags"])
