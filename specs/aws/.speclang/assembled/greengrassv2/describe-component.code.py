def describe_component(store, request: dict) -> dict:
    return store.describe_component(request["componentName"], request["componentVersion"])
