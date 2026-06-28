def handler(store, request: dict) -> dict:
    return store.describe_index(request['Id'])

