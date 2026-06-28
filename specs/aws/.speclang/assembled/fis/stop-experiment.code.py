def stop_experiment(store, request: dict) -> dict:
    return store.stop_experiment(request["id"])
