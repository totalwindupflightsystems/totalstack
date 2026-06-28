def stop_training_job(store, request: dict) -> dict:
    store.stop_training_job(request["TrainingJobName"])
    return {}
