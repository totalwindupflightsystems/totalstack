def handler(store, request: dict) -> dict:
    record = store.create_model_customization_job(request)
    return {"jobArn": record.jobArn}
