def handler(store, request: dict) -> dict:
    return store.delete_language_model(request["ModelName"])

