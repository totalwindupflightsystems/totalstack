def delete_retained_message(store, request: dict) -> dict:
    store.delete_retained_message(request["topic"])
    return {}
