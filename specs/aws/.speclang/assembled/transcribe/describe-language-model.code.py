def handler(store, request: dict) -> dict:
    return store.describe_language_model(request["ModelName"])

