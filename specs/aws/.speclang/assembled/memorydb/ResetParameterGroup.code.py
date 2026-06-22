def handler(store, request: dict) -> dict:
    return store.reset_parameter_group(**request)

