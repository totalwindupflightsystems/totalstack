def delete_experiment(store, request: dict) -> dict:
    store.delete_experiment(request["id"])
    return {}
