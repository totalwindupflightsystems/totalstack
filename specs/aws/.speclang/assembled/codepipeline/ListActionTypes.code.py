def handler(store, request: dict) -> dict:
    return store.list_action_types(
        action_owner_filter=request.get("actionOwnerFilter"),
        next_token=request.get("nextToken"),
        region_filter=request.get("regionFilter"),
    )
