def delete_training_job(store, request: dict) -> dict:
    store.delete_training_job(request["TrainingJobName"])
    return {}
