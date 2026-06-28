def describe_experiment(store, request: dict) -> dict:
    return store.describe_experiment(request["id"])
