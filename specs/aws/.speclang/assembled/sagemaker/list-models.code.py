def list_models(store, request: dict) -> dict:
    models = store.list_models()
    return {"Models": models}
