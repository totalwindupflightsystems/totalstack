def create_policy(store, request: dict) -> dict:
    return store.create_policy(**request)
