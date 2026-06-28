def handler(store, r: dict) -> dict:
    store.delete_model(r["modelId"], r["modelType"])
    return {}
