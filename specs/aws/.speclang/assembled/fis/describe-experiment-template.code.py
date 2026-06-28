def describe_experiment_template(store, request: dict) -> dict:
    return store.describe_experiment_template(request["id"])
