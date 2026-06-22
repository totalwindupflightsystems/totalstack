def handler(store, request: dict) -> dict:
    record = store.get_model_customization_job(request["jobIdentifier"])
    return record.to_dict()
