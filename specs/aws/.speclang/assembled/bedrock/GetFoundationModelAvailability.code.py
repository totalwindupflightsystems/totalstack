def handler(store, request: dict) -> dict:
    return store.get_foundation_model_availability(request["modelId"])
