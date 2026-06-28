def describe_model(store, request: dict) -> dict:
    return store.describe_model(request["ModelName"])
