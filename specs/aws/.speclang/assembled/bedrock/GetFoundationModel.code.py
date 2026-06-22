def handler(store, request: dict) -> dict:
    model = store.get_foundation_model(request["modelIdentifier"])
    return {"modelDetails": model.to_dict()}
