def handler(store, request: dict) -> dict:
    return store.get_action_type(
        category=request["category"],
        owner=request["owner"],
        provider=request["provider"],
        version=request["version"],
    )
