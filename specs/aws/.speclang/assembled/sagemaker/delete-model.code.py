def delete_model(store, request: dict) -> dict:
    store.delete_model(request["ModelName"])
    return {}
