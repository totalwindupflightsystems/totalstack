def get_retained_message(store, request: dict) -> dict:
    return store.get_retained_message(request["topic"])
