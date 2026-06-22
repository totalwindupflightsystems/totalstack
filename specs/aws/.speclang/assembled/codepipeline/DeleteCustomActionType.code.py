def handler(store, request: dict) -> dict:
    return store.delete_custom_action_type(
        category=request["category"],
        provider=request["provider"],
        version=request["version"],
    )
