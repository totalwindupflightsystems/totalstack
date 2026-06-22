def handler(store, request: dict) -> dict:
    return store.stop_model_customization_job(request["jobIdentifier"])
