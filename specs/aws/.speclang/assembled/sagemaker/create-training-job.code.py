def create_training_job(store, request: dict) -> dict:
    return store.create_training_job(**request)
