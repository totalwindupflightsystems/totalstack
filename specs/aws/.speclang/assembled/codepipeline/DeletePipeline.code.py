def handler(store, request: dict) -> dict:
    return store.delete_pipeline(name=request["name"])
