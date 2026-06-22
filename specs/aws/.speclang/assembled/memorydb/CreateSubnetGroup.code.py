def handler(store, request: dict) -> dict:
    return store.create_subnet_group(**request)

