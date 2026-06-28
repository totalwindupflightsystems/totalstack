def delete_experiment_template(store, request: dict) -> dict:
    store.delete_experiment_template(request["id"])
    return {}
