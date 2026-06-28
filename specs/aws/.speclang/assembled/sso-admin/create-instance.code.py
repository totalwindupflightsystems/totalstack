def handler(store, request: dict) -> dict:
    return store.create_instance(name=request.get("name"), tags=request.get("tags"))
