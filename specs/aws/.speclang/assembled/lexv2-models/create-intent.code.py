def create_intent(store, request: dict) -> dict:
    return store.create_intent(**request)
