def create_experiment_template(store, request: dict) -> dict:
    return store.create_experiment_template(**request)
