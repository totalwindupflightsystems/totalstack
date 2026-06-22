def delete_environment(store, request: dict) -> dict:
    return store.delete_environment(request["Name"])
