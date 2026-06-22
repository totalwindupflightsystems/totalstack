def handler(store, request: dict) -> dict:
    return store.update_action_type(action_type=request["actionType"])
