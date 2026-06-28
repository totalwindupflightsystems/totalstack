def delete_component(store, request: dict) -> dict:
    store.delete_component(request["componentName"], request["componentVersion"])
    return {}
