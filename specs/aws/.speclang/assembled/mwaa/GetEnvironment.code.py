def get_environment(store, request: dict) -> dict:
    return store.get_environment(request["Name"])
