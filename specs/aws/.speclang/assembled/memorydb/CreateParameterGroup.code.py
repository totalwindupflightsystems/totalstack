def handler(store, request: dict) -> dict:
    return store.create_parameter_group(**request)

