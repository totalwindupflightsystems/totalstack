def describe_training_job(store, request: dict) -> dict:
    return store.describe_training_job(request["TrainingJobName"])
