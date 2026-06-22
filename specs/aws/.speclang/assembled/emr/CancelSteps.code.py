def handler(store, request: dict) -> dict:
    store.cancel_steps(request["ClusterId"], request["StepIds"])
    return {}
