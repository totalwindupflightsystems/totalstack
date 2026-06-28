def handler(store, request: dict) -> dict:
    return store.delete_index(request['Id'])

