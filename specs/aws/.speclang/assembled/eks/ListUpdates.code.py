def handler(store, request: dict) -> dict:
    return store.list_updates(name=request["name"])
