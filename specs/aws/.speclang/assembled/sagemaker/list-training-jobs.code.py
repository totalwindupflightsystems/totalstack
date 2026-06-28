def list_training_jobs(store, request: dict) -> dict:
    jobs = store.list_training_jobs()
    return {"TrainingJobSummaries": jobs}
