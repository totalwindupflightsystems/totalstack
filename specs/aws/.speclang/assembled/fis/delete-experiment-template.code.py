def delete_experiment_template(store, request: dict) -> dict:
    return store.delete_experiment_template(request["id"])
