def create_thing(store, request: dict) -> dict:
    return store.create_thing(**request)
