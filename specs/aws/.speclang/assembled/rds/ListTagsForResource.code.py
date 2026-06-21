def handler(store, request: dict) -> dict:
    """ListTagsForResource handler."""
    return store.list_tags_for_resource(
        resource_name=request["ResourceName"])
