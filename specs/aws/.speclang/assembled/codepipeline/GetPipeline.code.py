def handler(store, request: dict) -> dict:
    return store.get_pipeline(name=request["name"])
